package Events;

// Исключение для ситуации, когда персонаж потерян
class CharacterNotFoundException extends Exception {
    public CharacterNotFoundException(String message) {
        super(message);
    }

    @Override
    public String getMessage() {
        return "Персонаж не найден: " + super.getMessage();
    }
}