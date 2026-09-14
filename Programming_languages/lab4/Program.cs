// https://raw.githubusercontent.com/sahildit/IMDB-Movies-Extensive-Dataset-Analysis/refs/heads/master/data1/IMDb%20movies.csv
using System.Globalization;
using System.Runtime.CompilerServices;
using System.Security.Cryptography.X509Certificates;
using Microsoft.VisualBasic.FileIO;

List<string[]> ReadAllCsvLines(string filePath)
{
    var result = new List<string[]>();

    using (var parser = new TextFieldParser(filePath))
    {
        parser.TextFieldType = FieldType.Delimited;
        parser.SetDelimiters(",");
        parser.HasFieldsEnclosedInQuotes = true;

        while (!parser.EndOfData)
        {
            string[] fields = parser.ReadFields();
            result.Add(fields);
        }
    }

    return result;
}

var splistr = "A, B, C".Split(',');
var intTest = int.TryParse("122", out var intResult) ? intResult : 0;
var filepath = "IMDb movies.csv";
var csvList = ReadAllCsvLines(filepath)
                                    .Select(film => new Movie()
                                    {
                                        imdb_title_id = film[0],
                                        title = film[1],
                                        original_title = film[2],
                                        year = int.TryParse(film[3], out var intResult) ? intResult : 0,
                                        date_published = film[4],
                                        genre = film[5],
                                        duration = film[6],
                                        country = film[7],
                                        language = film[8],
                                        director = film[9],
                                        writer = film[10],
                                        production_company = film[11],
                                        actors = film[12],
                                        description = film[13],
                                        avg_vote = double.TryParse(film[14], CultureInfo.InvariantCulture, out var Result14) ? Result14 : 0.0,
                                        votes = film[15],
                                        budget = film[16],
                                        usa_gross_income = film[17],
                                        worlwide_gross_income = film[18],
                                        metascore = film[19],
                                        reviews_from_users = double.TryParse(film[20], out var Result20) ? Result20 : 0.0,
                                        reviews_from_critics = double.TryParse(film[21], out var Result21) ? Result21 : 0.0
                                    }
);
Console.WriteLine("все фильмы режиссера Werner Herzog");
foreach (var item in csvList.Where(film => film.director.ToLower().Contains("werner herzog")))
{
     Console.Write(item.title + ", ");
};
Console.WriteLine("\n5 самый высокооценённых фильма выпущенных после 2010");
foreach (var item in csvList.Where(film => film.year >= 2010).OrderByDescending(Film => Film.avg_vote).Take(5))
{
     Console.Write(item.title + "(" + item.avg_vote + ")" + ", ");
};
Console.WriteLine("\nсписок фильмов (их количество и средний рейтинг) жанра History)");
var history_films = csvList.Where(film => film.genre.ToLower().Contains("history")).ToList();
var film_count = history_films.Count();
Console.Write("\nколичество " + film_count);
Console.Write("\nсредний рейтинг " + history_films.Aggregate(0.0, (srznach, film) => srznach += film.avg_vote) / film_count);
var directors = csvList.Select(film => film.director.ToLower()).ToList();
Console.Write("\nРежисёр у которого больше всего фильмов");
Console.Write("\n" + csvList.SelectMany(film => film.director.ToLower().Split(",")).GroupBy(x => x).OrderByDescending(x => x.Count()).First().FirstOrDefault());
//var directors = csvList.Select(film => film.director.ToLower()).Distinct().ToList();
//Console.Write("\n" + directors.OrderByDescending(Director => csvList.Where(film => film.genre.ToLower().Contains(Director)).Count()).Take(1));
// 1. Преобразовать в класс Movie (нужно создать класс) - Select
// Над списком из Movie 
// 2. Найти все фильмы режисёра/актёра/продюсера (на выбор, например Nolan) - Where
// 3. 5 самый высокооценённых фильма выпущенных после 2010 
// 4. Получить список фильмов (их количество и средний рейтинг) любого жанра (на выбор, например Drama) 
// 5. Режисёр у которого больше всего фильмов
// Не учитывать регистр
// Обработать поля с несколькими значениями