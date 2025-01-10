package Events;

// Абстрактный класс для всех обектов, взаимодействущих с персоонажами, но не явл. ими
public abstract class Creature {
    protected Location location;

    public Creature(Location location) {
        this.location = location;
    }

    public void interact(Character character) {}
}
