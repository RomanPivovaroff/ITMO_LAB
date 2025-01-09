package Events;

import java.util.Random;

// Класс Дочери Великана
public class GiantDaughter extends Character {
    public GiantDaughter(String name, Location location) {
        super(name, location);
    }

    @Override
    public void performAction() {
        System.out.println(this.name + "ждет принца" + this.location.getDescription());

        Random rand = new Random();
        int event = rand.nextInt(3); // Случайное событие (0 - нападение, 1 - встреча с принцем, 2 - спокойное ожидание)

        switch (event) {
            case 0: // забирается на дерево.
                this.state = State.PROTECTED;
                System.out.println(this.name + "забралась на дерево, чтобы подождать");
                break;
            case 1, 2: // Спокойное ожидание
                this.state = State.WAITING;
                System.out.println(this.name + "продолжает ждать" + this.location.getDescription);
                break;
            default:
                break;
        }
    }
}