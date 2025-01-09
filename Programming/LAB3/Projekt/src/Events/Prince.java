package Events;

import java.util.Random;
// а у меня тоже был принц в лабе
// Класс Принца
class Prince extends Character {
    public Prince(String name, Location location, Location[] locations) {
        super(name, location);
    }

    @Override
    public void performAction() {
        System.out.println(name + " ищет дочь великана.");

        Random rand = new Random();
        int event = rand.nextInt(3); // Случайное событие (0 - встречает дочь, 1 - продолжает поиски)

        switch (event) {
            case 0: // Принц находит дочь
                this.state = State.FOUND;
                System.out.println(name + " нашел дочь великана!");
                break;
            case 1: // Принц продолжает поиски
                this.state = State.SEARCHING;
                System.out.println(name + " продолжает искать дочь великана.");
                break;
            case 2:
                int death = rand.nextInt(2); // проверка на смерть принца от чудовища
                if (death == 1) this.state = State.DIED;
                else this.state = State.SEARCHING;
                break;
        }
    }
}