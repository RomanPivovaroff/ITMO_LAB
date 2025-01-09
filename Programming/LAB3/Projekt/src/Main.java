import Events.*;
//код не работает
public class Main {
    public static void main() {
        // Локации
        Location WellLocation = new Location("у старого каменного колодца");
        Location TreeLocation = new Location("на дереве возле колодца");
        Location forest = new Location("в лесу");
        Location Village = new Location("в деревне");
        Location Mountains = new Location("в горах");
        Location[] locations_for_prince = {forest, Mountains, WellLocation, TreeLocation};

        // Персонажи
        GiantDaughter giantDaughter = new GiantDaughter("Дочь Велекана", WellLocation);
        Giant giant = new Giant("Великан", Mountains);
        Prince prince = new Prince("Принц", Village, locations_for_prince);

        // Симуляция действий
        try {
            giant.performAction();
            prince.performAction();
            giantDaughter.performAction();

            tree.interact(giantDaughter);
            well.interact(giantDaughter);

            // Пример выбрасывания исключения, если персонаж не найден
            if (giantDaughter.state == State.ATTACKED) {
                throw new CharacterNotFoundException("Дочь Великана не может быть найдена из-за нападения.");
            }
        } catch (CharacterNotFoundException e) {
            System.out.println(e.getMessage());
        }
    }
}
