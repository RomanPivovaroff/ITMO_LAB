package Events;

import java.util.ArrayList;
import java.util.Random;

// Класс Великана
public class Giant extends Character implements SearchActions{
    private ArrayList<Location> GiantLocations;
    public Giant(String name, Location location, ArrayList<Location> locations) {
        super(name, location);
        this.GiantLocations = locations;
        this.state = State.LOST;
    }

    @Override
    public void performAction() {
        if (this.state == State.LOST) {
            System.out.println(name + " живет, даже не подозревая о существовании своей дочери.");
            Random rand = new Random();
            int event = rand.nextInt(2); // Случайное событие

            switch (event) {
                case 0: // Великан узнает о своей дочери
                    this.state = State.SEARCHING;
                    System.out.println(name + " узнал что у него есть дочь и хочет найти ее!");
                    break;
            }
        }
    }

    @Override
    public void Search(Location target_location) {
        System.out.println(name + " ищет свою дочь " + location.getDescription());

        // проверка находится ли гигант в той же локации что и принцесса
        if (target_location.equals(this.location)) {
            this.state = State.FOUND;
            System.out.println(name + " нашел свою дочь " + location.getDescription() + " и теперь ей не страшны волки!");
        }
        else {
            Random rand = new Random();
            System.out.println(this.name + " продолжает искать свою дочь.");
            int next_location_number = rand.nextInt(this.GiantLocations.size());
            this.location = this.GiantLocations.get(next_location_number);
            this.GiantLocations.remove(next_location_number);
            if (this.GiantLocations.size() == 0) {
                System.out.println(name + " нашел свою дочь " + target_location.getDescription() + " и теперь ей не страшны волки!");
                state = State.FOUND;
            }
        }
    }
}