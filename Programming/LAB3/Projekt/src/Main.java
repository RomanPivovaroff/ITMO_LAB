import Events.*;

import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main() {
        // Локации
        Location WellLocation = new Location("у старого каменного колодца");
        Location TreeLocation = new Location("на дереве возле колодца");
        Location forest = new Location("в лесу");
        Location Village = new Location("в деревне");
        Location Mountains = new Location("в горах");
        Location Desert = new Location("в пустыне");
        Location Lake = new Location("у озера");

        // создание массивов локаций для путишествий и поиска дочери великана
        Location[] massive_for_listP = new Location[] {forest, Mountains, WellLocation, Desert,  Lake};
        ArrayList<Location> locations_for_prince = new  ArrayList<Location>(Arrays.asList(massive_for_listP));
        Location[] massive_for_listG = new Location[] {forest, WellLocation, TreeLocation};
        ArrayList<Location> locations_for_giant = new  ArrayList<Location>(Arrays.asList(massive_for_listG));

        // Персонажи
        GiantDaughter giantDaughter = new GiantDaughter("Дочь Великана Элли", WellLocation);
        Giant giant = new Giant("Великан Михалыч", Mountains, locations_for_prince);
        Prince prince = new Prince("Принц Эдвард", Village, locations_for_prince);

        //сущности
        Tree tree = new Tree(TreeLocation);
        Wolf[] wolfs = new Wolf[] {new Wolf(forest), new Wolf(forest), new Wolf(forest), new Wolf(forest)};

        // Симуляция действий
        try {
            while (true) {
                // получаем исключения если дочь великана умерла
                if (giantDaughter.getInfo().state() == State.DIED) {
                    throw new CharacterNotFoundException("Дочь Великана погла при нападении волков.");
                }
                // получаем исключения если принц умер
                if (prince.getInfo().state() == State.DIED) {
                    throw new CharacterNotFoundException("Дочь Великана погла при нападении волков.");
                }
                // выходим из цикла если принц нашел дочь великана
                if (prince.getInfo().state() == State.FOUND) {
                    break;
                }
                // если дочь великана опасается волков она залезает на дерево
                if (giantDaughter.getInfo().state() == State.AFRAID) {
                    tree.interact(giantDaughter);
                }
                //принцесса выполняет свое действие(ждет или начинает переживать и боятся волков)
                giantDaughter.performAction();
                // определяем локацию дочери великана
                Location location_giantDaugher = giantDaughter.getInfo().location();
                // Великан выполняет либо действие(если не знает о сущ. свой дочери) либо поиск
                if (giant.getInfo().state() == State.LOST) {giant.performAction();}
                else {giant.Search(location_giantDaugher);}
                // принц ищет дочь великана, выполняет действие в слуае неудачи
                prince.Search(location_giantDaugher);
                // если великан находит свою дочь волки не ходят, потому что опасаются его
                if (giant.getInfo().state() != State.FOUND) {
                    // ход волков. поиск жертвы и нападение в случае успеха
                    for (var i = 0; i < wolfs.length; i++) {
                        wolfs[i].Search(location_giantDaugher);
                        wolfs[i].interact(giantDaughter);
                    }
                }
            }
        } catch (CharacterNotFoundException e) {
            System.out.println(e.getMessage());
        }
    }
}
