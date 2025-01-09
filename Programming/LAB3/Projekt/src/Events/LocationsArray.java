package Events;

import java.util.Random;

public class LocationsArray {
    private Location[] locations;

    public LocationsArray() {
        Location Well = new Location("у старого каменного колодца");
        Location Tree = new Location("на дереве возле колодца");
        Location forest = new Location("в лесу");
        Location Village = new Location("в деревне");
        Location Mountains = new Location("в горах");
        Location[] locations = {forest, Village, Mountains, Tree, Well};
    }
    // хрень написал
    public Location getStartGiantDaugherLocation() {
        Random rand = new Random();
        final int START_LOCATION_GIANT_GAUGHER = 4; //  стартовая локция дочери великана
        return this.locations[START_LOCATION_GIANT_GAUGHER];
    }

    public Location getStartOthersRandomLocation() {
        Random rand = new Random();
        int location = rand.nextInt(3); // Случайная стартовая локция
        return this.locations[location];
    }
}