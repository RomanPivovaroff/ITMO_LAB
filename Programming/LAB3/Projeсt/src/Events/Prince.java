package Events;

import java.util.ArrayList;
import java.util.Random;

// Класс Принца
public class Prince extends Character implements SearchActions{
    private int strenght;
    private ArrayList<Location> PrinceLocations;
    public Prince(String name, Location location, ArrayList<Location> locations) {
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
            case 2:
                System.out.println(this.name + " находит " + this.location.getDescription() + " чудовище и сражается с ним.");
                int death = rand.nextInt(2 + this.strenght); // проверка на смерть принца от чудовища
                if (death == 1) {
                    System.out.println("чудовище оказалось сильнее.");
                    this.state = State.DIED;
                }
                else {
                    System.out.println(this.name + " выходит победителем из этой неравной схватки.");
                    this.strenght += 1;
                    this.state = State.SEARCHING;
                }
                break;
        }
        int next_location_number = rand.nextInt(this.PrinceLocations.size());
        this.location = this.PrinceLocations.get(next_location_number);
        this.PrinceLocations.remove(next_location_number);
    }

    @Override
    public void Search(Location target_location) {
        if (this.PrinceLocations.size() == 0) {
            System.out.println(name + " нашел дочь великана " + target_location.getDescription());
            state = State.FOUND;
        }
        else {
            System.out.println(name + " ищет дочь великана " + location.getDescription());

            // проверка находится ли принц в той же локации что и принцесса
            if (target_location.equals(this.location)) {
                this.state = State.FOUND;
                System.out.println(name + " нашел дочь великана!");
            } else {
                performAction();
            }
        }
    }
}