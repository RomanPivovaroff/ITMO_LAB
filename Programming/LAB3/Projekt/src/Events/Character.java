package Events;

// Абстрактный класс для всех персонажей
abstract class Character implements Action {
    protected String name;
    protected State state;
    protected Location location;

    public Character(String name, Location location) {
        this.name = name;
        this.location = location;
        this.state = State.WAITING; // Изначально персонаж в ожидании
    }

    @Override
    public void performAction() {
        // Абстрактный метод для действий, который будет реализован в наследниках
    }

    @Override
    public String toString() {
        return name + " находится в " + location.getDescription() + " и в состоянии " + state;
    }
}