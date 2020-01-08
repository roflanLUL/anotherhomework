let a = document.getElementById("santa_count").innerHTML;
let b = document.getElementById("elves_count").innerHTML;
let c = document.getElementById("mail_count").innerHTML;
load_scores_post();

function load_scores() {
    document.getElementById("santa_count").innerHTML = a;
    document.getElementById("elves_count").innerHTML = b;
    document.getElementById("mail_count").innerHTML = c;
}

function load_scores_post() {
    document.getElementById("id_santa_score").setAttribute('value', a);
    document.getElementById("id_elves_score").setAttribute('value', b);
    document.getElementById("id_mail_score").setAttribute('value', c);
}

function santa_func() {
    a++;
    load_scores();
    load_scores_post();
}

function elves_func() {
    b++;
    load_scores();
    load_scores_post();
}

function mail_func() {
    <!-- Да, я смог прочитать ту самую надпись -->
    alert("Мужчина, вы что не видите? У нас перерыв!!!");
    load_scores();
    load_scores_post();
}

function all_func() {
    a++;
    b++;
    c++;
    load_scores();
    load_scores_post();
}