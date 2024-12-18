package Events;

import java.util.Random;

// Класс Великана
class Giant extends Character {
    public Giant(String name, Location location) {
        super(name, location);
    }

    @Override
    public void performAction() {
        System.out.println(name + " ищет свою дочь.");

        Random rand = new Random();
        int event = rand.nextInt(2); // Случайное событие (0 - находит дочь, 1 - теряет след)

        switch (event) {
            case 0: // Великан находит дочь
                this.state = State.FOUND;
                System.out.println(name + " нашел свою дочь!");
                break;
            case 1: // Великан теряет след
                this.state = State.LOST;
                System.out.println(name + " потерял след своей дочери.");
                break;
            default:
                break;
        }
    }
}