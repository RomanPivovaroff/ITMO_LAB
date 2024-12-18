package Events;

import java.util.Random;

// Класс Дочери Великана
class GiantDaughter extends Character {
    public GiantDaughter(String name, Location location) {
        super(name, location);
    }

    @Override
    public void performAction() {
        System.out.println(name + " ждет на дереве, опасаясь волков.");

        Random rand = new Random();
        int event = rand.nextInt(3); // Случайное событие (0 - нападение, 1 - встреча с принцем, 2 - спокойное ожидание)

        switch (event) {
            case 0: // Нападение волков
                this.state = State.ATTACKED;
                System.out.println(name + " была атакована волками!");
                break;
            case 1: // Встреча с принцем
                this.state = State.FOUND;
                System.out.println(name + " была найдена принцем!");
                break;
            case 2: // Спокойное ожидание
                this.state = State.WAITING;
                System.out.println(name + " продолжает ждать на дереве.");
                break;
            default:
                break;
        }
    }
}