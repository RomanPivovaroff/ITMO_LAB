package Events;


import java.util.Random;

public class Wolf extends Creature implements SearchActions{
    public Wolf(Location location) {super(location);}

    @Override
    public void interact(Character character) {
        if (character instanceof GiantDaughter) {
            if (character.location.equals(location)) {
                if (character.state != State.PROTECTED) {
                    System.out.println("Волк надает на " + character.name + ' ' + location.getDescription());
                    character.state = State.DIED;
                }
            }
        }
    }

    @Override
    public void Search(Location target_location) {
        Random rand = new Random();
        System.out.println("волк пытается найти пищу " + this.location);
        int find_trail = rand.nextInt(6); // попытка волка найти след жертвы
        if (find_trail == 1) {
            System.out.println("волк что-то почуял.");
            this.location = target_location;
        }
    }
}
