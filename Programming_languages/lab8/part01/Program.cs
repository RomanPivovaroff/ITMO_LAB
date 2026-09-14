using part01;
using System.Reflection;

var engine = new SkillEngine();


// 1. Запустили примеры
// Делаем всё в part01
// 2. Написать класс, на которой повесили атрибут GameAttribute 
// 3. Создать два метода в этом классе с атрибутами CombatSkillAttribute 
// С тригерами (OnDefense и на PostBattle)
// 4. OnDefense снижение урона в два раза
// 5. PostBattle у Attacker и Defender снижается HP на 10
// 6. Вызвать попорядку pipeline OnDefense => OnAttack => PostBattle
// 7. 4 и 5 пункт математику сделать с помощью ILGenerator
// Не использовать инструкции Call, CallVirt и т.д.
// Не использовать (typeof()).GetField() GetProperties() 

// Регистрация текущей сборки (или загрузка внешней DLL)
engine.RegisterAssembly(Assembly.GetExecutingAssembly());

// Симуляция контекста боя
var context = new BattleContext
{
    DamageDealt = 100,
    Attacker = new UnitStats { Hp = 50 },
    Defender = new UnitStats { Hp = 100 }
};

// Рефлексия — это процесс анализа внутреннего устройства программы (во время выполнения). 
// Возможноcть модифицировать внутрнние структуры и функции.
// 1. Обработка атрибутов
// 2. Получить доступ до скрытых методов или полей
// 3. Когда это действительно нужно

Console.WriteLine("--- Starting Attack Phase ---");

// Ядро само находит нужные методы и вызывает их в правильном порядке (сначала Crit, потом Vampirism)
engine.ExecutePipeline(TriggerType.OnDefense, context);
engine.ExecutePipeline(TriggerType.OnAttack, context);
engine.ExecutePipeline(TriggerType.PostBattle, context);

Console.WriteLine($"Attacker Final HP: {context.Attacker.Hp}"); 
Console.WriteLine($"Defender Final HP: {context.Defender.Hp}");

