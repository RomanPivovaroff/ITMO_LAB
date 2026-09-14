using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace part01
{
    [GameAttribute]
    public class ShildMechanics
    {
        // Декларативная разметка: этот метод должен сработать при атаке защите
        [CombatSkill("Shild", TriggerType.OnDefense)]
        public void Shild(BattleContext ctx)
        {
            var beforeDamage =  ctx.DamageDealt;
            var fastDelegate = Examples.Division();
            ctx.DamageDealt = fastDelegate(ctx.DamageDealt, 2);
            Console.WriteLine($"[System] Shild activation: change damage {beforeDamage} to {ctx.DamageDealt}.");
        }

        [CombatSkill("AllDamage", TriggerType.PostBattle)]
        public void AllDamage(BattleContext ctx)
        {
            var fastDelegate = Examples.Minus();
            ctx.Attacker.Hp = fastDelegate(ctx.Attacker.Hp, 10);
            ctx.Defender.Hp = fastDelegate(ctx.Defender.Hp, 10);;
            Console.WriteLine($"[System] All Damage!");
        }
    }
}
