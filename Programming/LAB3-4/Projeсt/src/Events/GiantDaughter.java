package Events;

import java.util.Random;

// Класс Дочери Великана
public class GiantDaughter extends Character {
    public GiantDaughter(String name, Location location) {
        super(name, location);
    }

    @Override
    public void performAction() {
        System.out.println(this.name + " ждет принца " + this.location.getDescription());

        if (this.state != State.PROTECTED) {
            Random rand = new Random();
            int event = rand.nextInt(3); // Случайное событие

            switch (event) {
                case 0: //  опасаетмя нападения волков
                    System.out.println(this.name + " опасается нападения волков");
                    this.state = State.AFRAID;
                    break;
                case 1, 2: // Спокойное ожидание
                    this.state = State.WAITING;
                    System.out.println(this.name + " продолжает ждать " + this.location.getDescription());
                    break;
                default:
                    break;
            }
        }
    }
}