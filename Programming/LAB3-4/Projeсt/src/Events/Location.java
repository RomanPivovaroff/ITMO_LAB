package Events;

// Класс для Локаций
public class Location {
    private final String description;

    public Location(String description) {
        this.description = description;
    }

    public String getDescription() {
        return description;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == null || obj.getClass() != this.getClass()) {
            return false;
        }
        Location other_location = (Location) obj;
        return description.equals(other_location.getDescription());
    }

    @Override
    public int hashCode() {
        int total = 31;
        total = 31 * total + (description == null ? 0 : description.hashCode());
        return total;
    }
    @Override
    public String toString() {
        return "персонажи будут находится " + description;
    }
}