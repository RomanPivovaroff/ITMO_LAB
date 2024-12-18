package Events;

// Класс для Колодца
class Well {
    private Location location;

    public Well(Location location) {
        this.location = location;
    }

    public void interact(Character character) {
        if (character instanceof GiantDaughter) {
            System.out.println(character.name + " ждет у колодца.");
        }
    }
}
