package Events;

import java.util.Random;

public class LocationsArray {
    private Location[] locations;

    public LocationsArray() {
        Location wellLocation = new Location("у старого каменного колодца");
        Location treeLocation = new Location("на дереве возле колодца");
        Location forestLocation = new Location("в лесу");
        Location VillageLocation = new Location("в деревне");
        this.locations = {forestLocation, VillageLocation, treeLocation, wellLocation};
    }

    public Location[] getStartGiantDaugherLocation() {
        Random rand = new Random();
        int location = 4 //  стартовая локция дочери великана
        return locations[location];
    }
    public Location[] getStartOthersRandomLocation() {
        Random rand = new Random();
        int location = rand.nextInt(3); // Случайная стартовая локция
        return locations[location];
    }
}