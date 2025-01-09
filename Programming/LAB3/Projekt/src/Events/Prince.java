package Events;

import java.util.Random;

// Класс Принца
public class Prince extends Character implements SearchActions{
    private int strenght;
    private Location[] PrinceLocations;
    public Prince(String name, Location location, Location[] locations) {
        super(name, location);
        this.strenght = 0;
        this.PrinceLocations = locations;
    }

    @Override
    public void performAction() {
        Random rand = new Random();
        int event = rand.nextInt(3); // Случайное событие (0, 1 - продолжает поиски, 2 - встречает чудовище)

        switch (event) {
            case 0, 1: // Принц продолжает поиски
                this.state = State.SEARCHING;
                System.out.println(this.name + " продолжает искать дочь великана.");
                this.location = this.PrinceLocations[event];
                break;
            case 2:
                System.out.println(this.name + " находит в " + this.location + "чудовище и сражается с ним.");
                int death = rand.nextInt(2 + this.strenght); // проверка на смерть принца от чудовища
                if (death == 1) {
                    System.out.println("чудовище оказалось сильнее.");
                    this.state = State.DIED;
                }
                else {
                    System.out.println(this.name + "выходит победителем из этой неравной схватки.");
                    this.state = State.SEARCHING;
                }
                break;
        }
    }

    @Override
    public void Search() {
        System.out.println(name + " ищет дочь великана.");

        Random rand = new Random();
        int event = rand.nextInt(2); // Случайное событие (0 - находит дочь, 1,2 - совершает действие)
        switch (event) {
            case 0: // Принц находит дочь
                this.state = State.FOUND;
                System.out.println(name + " нашел дочь великана!");
                break;
            case 1, 2: // Принц совершает действие
                performAction();
                break;
        }
    }
}