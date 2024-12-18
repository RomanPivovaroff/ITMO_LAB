import Events.*;

public class Main {
    public static void main(String[] args) {
        // Локации
        LocationsArray LocationsArray = new LocationsArray()

        // Персонажи
        GiantDaughter giantDaughter = new GiantDaughter("Дочь Великана", LocationsArray.getStartGiantDaugherLocation());
        Giant giant = new Giant("Великан", LocationsArray.getStartOthersRandomLocation());
        Prince prince = new Prince("Принц", LocationsArray.getStartOthersRandomLocation());

        // Объекты
        Tree tree = new Tree(treeLocation);
        Well well = new Well(wellLocation);

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
