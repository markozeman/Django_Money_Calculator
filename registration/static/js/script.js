document.addEventListener("DOMContentLoaded", main);

var submit;
var uporabniki = [];
var trenutni_uporabnik;


class Uporabnik {
    constructor(uporabnisko_ime, geslo) {
        this.uporabnisko_ime = uporabnisko_ime;
        this.geslo = geslo;
        this.bancno_stanje = new Stanje("banka");
        this.denarnica_stanje = new Stanje("denarnica");
        this.cilji = [];
        this.transakcije = [];
    }
    
    setUporabniskoIme (novo_up_ime) {
        this.uporabnisko_ime = novo_up_ime;
    }
    
    setGeslo (novo_geslo) {
        this.geslo = novo_geslo;
    }
    
    addCilj (nov_cilj) {
        this.cilji.push(nov_cilj);
    }
    
    getOpisCiljev () {
        var opis_ciljev = [];
        for (var i=0; i<this.cilji.length; i++) {
            opis_ciljev.push(this.cilji[i].opis);
        }
        return opis_ciljev;
    }
    
    findCilj (opis_cilja) {
        for (var i=0; i<this.cilji.length; i++) {
            if (this.cilji[i].opis == opis_cilja) {
                return this.cilji[i];
            }
        }
        return "Cilj s takim opisom ne obstaja";
    }
    
    addTranskacija (nova_transakcija) {
        this.transakcije.push(nova_transakcija);
    }
    
    executeTransakcija (transakcija) {
        var znesek = parseInt(transakcija.znesek);
        if (transakcija.smer == "polog") {
            this.denarnica_stanje.stanje -= znesek;
            this.bancno_stanje.stanje += znesek;
        }
        else if (transakcija.smer == "dvig") {
            this.bancno_stanje.stanje -= znesek;
            this.denarnica_stanje.stanje += znesek;
        }
    }
    
    executeIzdatekPrejemek (izdatek_prejemek) {
        var znesek = parseInt(izdatek_prejemek.znesek);
        var banka_denarnica = izdatek_prejemek.banka_denarnica;
        
        if (izdatek_prejemek.tip == "izdatek") {
            if (banka_denarnica == "denarnica") {
                this.denarnica_stanje.stanje -= znesek;
            }
            else if (banka_denarnica == "banka") {
                this.bancno_stanje.stanje -= znesek;
            }
        }
        else if (izdatek_prejemek.tip == "prejemek") {
            if (banka_denarnica == "denarnica") {
                this.denarnica_stanje.stanje += znesek;
            }
            else if (banka_denarnica == "banka") {
                this.bancno_stanje.stanje += znesek;
            }
        }
    }
    
    findAll (denarnica_banka_skupaj, izdatek_prejemek, casovno_obdobje, kategorija) {
        var izdatki = [];
        var prejemki = [];
        if (denarnica_banka_skupaj == "denarnica") {
            if (izdatek_prejemek == "izdatek") {
                for (var i=0; i<this.denarnica_stanje.izdatki.length; i++) {
                    var trenutni_izdatek = this.denarnica_stanje.izdatki[i];
                    if (Cilj.vZadnjemCasu(new Date(), trenutni_izdatek.datum, casovno_obdobje) && (trenutni_izdatek.kategorija == kategorija || kategorija == "vse")) {
                        izdatki.push(trenutni_izdatek);
                    }
                }
                return izdatki;
            }
            else if (izdatek_prejemek == "prejemek") {
                for (var i=0; i<this.denarnica_stanje.prejemki.length; i++) {
                    var trenutni_prejemek = this.denarnica_stanje.prejemki[i];
                    if (Cilj.vZadnjemCasu(new Date(), trenutni_prejemek.datum, casovno_obdobje) && (trenutni_prejemek.kategorija == kategorija || kategorija == "vse")) {
                        prejemki.push(trenutni_prejemek);
                    }
                }
                return prejemki;
            }
        }
        else if (denarnica_banka_skupaj == "banka") {
            if (izdatek_prejemek == "izdatek") {
                for (var i=0; i<this.bancno_stanje.izdatki.length; i++) {
                    var trenutni_izdatek = this.bancno_stanje.izdatki[i];
                    if (Cilj.vZadnjemCasu(new Date(), trenutni_izdatek.datum, casovno_obdobje) && (trenutni_izdatek.kategorija == kategorija || kategorija == "vse")) {
                        izdatki.push(trenutni_izdatek);
                    }
                }
                return izdatki;
            }
            else if (izdatek_prejemek == "prejemek") {
                for (var i=0; i<this.bancno_stanje.prejemki.length; i++) {
                    var trenutni_prejemek = this.bancno_stanje.prejemki[i];
                    if (Cilj.vZadnjemCasu(new Date(), trenutni_prejemek.datum, casovno_obdobje) && (trenutni_prejemek.kategorija == kategorija || kategorija == "vse")) {
                        prejemki.push(trenutni_prejemek);
                    }
                }
                return prejemki;
            }
        }
        else if (denarnica_banka_skupaj == "skupaj") {
            if (izdatek_prejemek == "izdatek") {
                for (var i=0; i<this.denarnica_stanje.izdatki.length; i++) {
                    var trenutni_izdatek = this.denarnica_stanje.izdatki[i];
                    if (Cilj.vZadnjemCasu(new Date(), trenutni_izdatek.datum, casovno_obdobje) && (trenutni_izdatek.kategorija == kategorija || kategorija == "vse")) {
                        izdatki.push(trenutni_izdatek);
                    }
                }
                for (var i=0; i<this.bancno_stanje.izdatki.length; i++) {
                    var trenutni_izdatek = this.bancno_stanje.izdatki[i];
                    if (Cilj.vZadnjemCasu(new Date(), trenutni_izdatek.datum, casovno_obdobje) && (trenutni_izdatek.kategorija == kategorija || kategorija == "vse")) {
                        izdatki.push(trenutni_izdatek);
                    }
                }
                return izdatki;
            }
            else if (izdatek_prejemek == "prejemek") {
                for (var i=0; i<this.denarnica_stanje.prejemki.length; i++) {
                    var trenutni_prejemek = this.denarnica_stanje.prejemki[i];
                    if (Cilj.vZadnjemCasu(new Date(), trenutni_prejemek.datum, casovno_obdobje) && (trenutni_prejemek.kategorija == kategorija || kategorija == "vse")) {
                        prejemki.push(trenutni_prejemek);
                    }
                }
                for (var i=0; i<this.bancno_stanje.prejemki.length; i++) {
                    var trenutni_prejemek = this.bancno_stanje.prejemki[i];
                    if (Cilj.vZadnjemCasu(new Date(), trenutni_prejemek.datum, casovno_obdobje) && (trenutni_prejemek.kategorija == kategorija || kategorija == "vse")) {
                        prejemki.push(trenutni_prejemek);
                    }
                }
                return prejemki;
            }
        }
    }
}


class Stanje {
    constructor(tip) {
        this.tip = tip;
        this.stanje = 0;
        this.izdatki = [];
        this.prejemki = [];
    }
    
    setZacetnoStanje (zacetno_stanje) {
        this.stanje = zacetno_stanje;
    }
    
    addIzdatekPrejemek (nov_izdatek_prejemek) {
        if (nov_izdatek_prejemek.tip == "izdatek") {
            this.izdatki.push(nov_izdatek_prejemek);
        }
        else if (nov_izdatek_prejemek.tip == "prejemek") {
            this.prejemki.push(nov_izdatek_prejemek);
        }
    }
}


class Cilj {
    constructor(opis, vrednost, do_datuma) {
        this.opis = opis;
        this.vrednost = vrednost;
        this.trenutno_privarcevano = 0;
        this.od_datuma = new Date();
        this.do_datuma = do_datuma;
    }
    
    povecajTrenutnoPrivarcevano (znesek) {
        this.trenutno_privarcevano += znesek;
    }
    
    stanjeVarcevanja() {
        return (this.trenutno_privarcevano / this.vrednost);
    }
    
    steviloDniMedDatumoma (datum_1, datum_2) {
        var timeDiff = Math.abs(datum_1.getTime() - datum_2.getTime());
        var diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24)); 
        return diffDays;
    }
    
    casovnoStanje() {
        var danes = new Date();
        var skupno = this.steviloDniMedDatumoma(this.od_datuma, this.do_datuma);
        var do_danes = this.steviloDniMedDatumoma(danes, this.do_datuma);
        return (do_danes / skupno);
    }
    
    vZadnjemCasu (danes, datum, casovno_obdobje) {
        if (casovno_obdobje == "teden" && this.steviloDniMedDatumoma(danes, datum) <= 7) {
            return true;
        }
        if (casovno_obdobje == "mesec" && this.steviloDniMedDatumoma(danes, datum) <= 31) {
            return true;
        }
        if (casovno_obdobje == "leto" && this.steviloDniMedDatumoma(danes, datum) <= 365) {
            return true;
        }
        return false;
    }
}


class IzdatekPrejemek {
    constructor(tip, opis, znesek, kategorija, banka_denarnica) {
        this.tip = tip;
        this.opis = opis;
        this.znesek = znesek;
        this.kategorija = kategorija;
        this.datum = new Date();
        this.banka_denarnica = banka_denarnica;
    }
}


class Transakcija {
    constructor(opis, znesek, smer) {
        this.opis = opis;
        this.znesek = znesek;
        this.smer = smer;   // polog/dvig
    }
}




function main() {
    

    
}




trenutni_uporabnik = new Uporabnik("marko", "geslo123");



function registration() {
    var inputs = document.getElementById("registration_form");
    
    var username = inputs[0];
    var password = inputs[1];
    var password_2 = inputs[2];
    
    var checkbox = document.getElementById("registration_form").elements["captcha"].checked;
    if (!checkbox) {
        alert ("Označite, da niste robot.");
        return;
    }
    
    if (submit.value == "Vpis") {
        if (username.value.length == 0) {
            alert("Vnesite uporabniško ime.");
            return;
        }
        if (username.value.length < 6) {
            alert("Uporabniško ime mora biti dolgo vsaj 6 znakov.");
            return;
        }
        
        // preveri, če je pravo uporabniško ime in pravilno geslo na vsaj enem od polj
        var user = find_user_by_username(username.value);
        if (typeof(user) !== 'string') {   // obstaja tak username
            if (user.geslo == password.value || user.geslo == password_2.value) {
                // TODO
                // vpiši uporabnika
                console.log("VPIS");
                window.location.href = "index.html";
            }   
            else {
                alert("Geslo je napačno.");
            }
        }
        else {
            alert("Uporabniško ime ne obstaja.");
        }
    }
    else if (submit.value == "Registracija") {
        if (username.value.length == 0 || password.value.length == 0 || password_2.value.length == 0) {
            alert("Izpolnite vsa polja.");
            return;
        }
        
        if (username.value.length < 6) {
            alert("Uporabniško ime mora biti dolgo vsaj 6 znakov.");
            return;
        }
        if (password.value != password_2.value) {
            alert("Gesli se ne ujemata.");
            return;
        }
        
        // preveri če tako uporabniško ime še ne obstaja, sicer pa registriraj novo osebo in ga dodaj v seznam uporabnikov
        var ze_obstaja = false;
        for (var i=0; i<uporabniki.length; i++) {
            if (username.value == uporabniki[i].uporabnisko_ime) {
                alert("To uporabniško ime že obstaja.");
                ze_obstaja = true;
            }
        }
        if(!ze_obstaja) {
            var uporabnik = new Uporabnik(username.value, password.value);
            trenutni_uporabnik = uporabnik;
            uporabniki.push(uporabnik);
        }
        
        console.log(uporabniki);
    }
    
    
    return false;
}


function get_visual_minus() {
    // preveri kateri dropdown je izbran
    var dropdown = document.getElementById("select_vizualizacija");
    var dropdown_string = dropdown.options[dropdown.selectedIndex].value;
    
    var inputs = document.getElementById("get_visual_minus");
    var kategorija = inputs[0].value;
    var casovno_obdobje = inputs[1].value;
    /*
    console.log(dropdown_string);
    console.log(kategorija);
    console.log(casovno_obdobje);
    */
    
    var result;
    if (dropdown_string == "wallet") {
        result = trenutni_uporabnik.findAll("denarnica", "izdatek", casovno_obdobje, kategorija);
    }
    else if (dropdown_string == "bank") {
        result = trenutni_uporabnik.findAll("banka", "izdatek", casovno_obdobje, kategorija);
    }
    else if (dropdown_string == "wallet_and_bank") {
        result = trenutni_uporabnik.findAll("skupaj", "izdatek", casovno_obdobje, kategorija);
    }
    
    // TODO
    // prikaži result
    
    // opis; znesek; kategorija; datum;
    
    var izdatek = new IzdatekPrejemek("izdatek", "čokolada", 3, "hrana", "denarnica");
    var izdatek_1 = new IzdatekPrejemek("izdatek", "bonboni", 2, "hrana", "denarnica");
    var izdatek_2 = new IzdatekPrejemek("izdatek", "coca-cola", 1, "hrana", "denarnica");
    var izdatek_3 = new IzdatekPrejemek("izdatek", "pizza", 6, "hrana", "denarnica");
    
    var max_vrednost = 6;
    var max_width = 150;
    var y = 30;
    
    var c = document.getElementById("izdatki_canvas");
    var ctx = c.getContext("2d");
    ctx.font = "20px Helvetica";
    
    ctx.fillText(izdatek.opis, 10, y, 100);
    ctx.fillText(izdatek_1.opis, 10, y*2, 100);
    ctx.fillText(izdatek_2.opis, 10, y*3, 100);
    ctx.fillText(izdatek_3.opis, 10, y*4, 100);
    
    ctx.fillStyle="#80ff80";
    ctx.fillRect(120, y-17, (izdatek.znesek / max_vrednost) * max_width, 20);
    ctx.fillRect(120, y*2-17, (izdatek_1.znesek / max_vrednost) * max_width, 20);
    ctx.fillRect(120, y*3-17, (izdatek_2.znesek / max_vrednost) * max_width, 20);
    ctx.fillRect(120, y*4-17, (izdatek_3.znesek / max_vrednost) * max_width, 20);
    
    
    return false;
}


function get_visual_plus() {
    // preveri kateri dropdown je izbran
    var dropdown = document.getElementById("select_vizualizacija");
    var dropdown_string = dropdown.options[dropdown.selectedIndex].value;
    
    var inputs = document.getElementById("get_visual_plus");
    var kategorija = inputs[0].value;
    var casovno_obdobje = inputs[1].value;
    /*
    console.log(dropdown_string);
    console.log(kategorija);
    console.log(casovno_obdobje);
    */
    
    var result;
    if (dropdown_string == "wallet") {
        result = trenutni_uporabnik.findAll("denarnica", "prejemek", casovno_obdobje, kategorija);
    }
    else if (dropdown_string == "bank") {
        result = trenutni_uporabnik.findAll("banka", "prejemek", casovno_obdobje, kategorija);
    }
    else if (dropdown_string == "wallet_and_bank") {
        result = trenutni_uporabnik.findAll("skupaj", "prejemek", casovno_obdobje, kategorija);
    }
    
    // TODO
    // prikaži result
    
    // opis; znesek; kategorija; datum;
    
    var prejemek = new IzdatekPrejemek("prejemek", "Plača_9_2016", 1000, "plača", "banka");
    var prejemek_1 = new IzdatekPrejemek("prejemek", "Plača_10_2016", 1111, "plača", "banka");
    var prejemek_2 = new IzdatekPrejemek("prejemek", "Plača_11_2016", 1300, "plača", "banka");
    
    var max_vrednost = 1300;
    var max_width = 150;
    var y = 30;
    
    var c = document.getElementById("prejemki_canvas");
    var ctx = c.getContext("2d");
    ctx.font = "20px Helvetica";
    
    ctx.fillText(prejemek.opis, 10, y, 100);
    ctx.fillText(prejemek_1.opis, 10, y*2, 100);
    ctx.fillText(prejemek_2.opis, 10, y*3, 100);
    
    ctx.fillStyle="#80ff80";
    ctx.fillRect(120, y-17, (prejemek.znesek / max_vrednost) * max_width, 20);
    ctx.fillRect(120, y*2-17, (prejemek_1.znesek / max_vrednost) * max_width, 20);
    ctx.fillRect(120, y*3-17, (prejemek_2.znesek / max_vrednost) * max_width, 20);
    
    
    return false;
}


function get_data() {
    // preveri kateri dropdown je izbran
    var dropdown = document.getElementById("pregled_select");
    var dropdown_string = dropdown.options[dropdown.selectedIndex].value;
    
    if (dropdown_string == "goals") {
        // prikaži cilje
    }
    else {
        // podatki iz forme
        var inputs = document.getElementById("pregled_form");
        var kategorija = inputs[0].value;
        var casovno_obdobje = inputs[1].value;
        
        console.log(dropdown_string);
        console.log(kategorija);
        console.log(casovno_obdobje);
        
        // TODO
        // izpiši glede na kategorijo in casovno_obdobje
        
        if (dropdown_string == "wallet") {
            
        }
        else if (dropdown_string == "bank") {
            
        }
    }
    



    
    return false;
}


function add_or_take_money() {
    // preveri kateri dropdown je izbran
    var dropdown = document.getElementsByClassName("select_dropdown")[0];
    var dropdown_string = dropdown.options[dropdown.selectedIndex].value;
    
    var inputs = document.getElementById("add_data");
    var opis = inputs[0].value;
    var znesek = inputs[1].value;
    var kategorija = inputs[2].value;
    /*
    console.log(opis);
    console.log(znesek);
    console.log(kategorija);
    */
    if (kategorija == "dvig" || kategorija == "polog") {
        var transakcija = new Transakcija(opis, znesek, kategorija);
        trenutni_uporabnik.addTranskacija(transakcija);
        trenutni_uporabnik.executeTransakcija(transakcija);
    }
    else {
        var izdatek_prejemek; 
        if (submit.value == "Dodaj") {
            if (dropdown_string == "wallet") {
                izdatek_prejemek = new IzdatekPrejemek("prejemek", opis, znesek, kategorija, "denarnica");
                trenutni_uporabnik.denarnica_stanje.addIzdatekPrejemek(izdatek_prejemek);
            }
            else if (dropdown_string == "bank") {
                izdatek_prejemek = new IzdatekPrejemek("prejemek", opis, znesek, kategorija, "banka");
                trenutni_uporabnik.bancno_stanje.addIzdatekPrejemek(izdatek_prejemek);
            }
        }
        else if (submit.value == "Odvzemi") {
            if (dropdown_string == "wallet") {
                izdatek_prejemek = new IzdatekPrejemek("izdatek", opis, znesek, kategorija, "denarnica");
                trenutni_uporabnik.denarnica_stanje.addIzdatekPrejemek(izdatek_prejemek);
            }
            else if (dropdown_string == "bank") {
                izdatek_prejemek = new IzdatekPrejemek("izdatek", opis, znesek, kategorija, "banka");
                trenutni_uporabnik.bancno_stanje.addIzdatekPrejemek(izdatek_prejemek);
            }
        }
        
        trenutni_uporabnik.executeIzdatekPrejemek(izdatek_prejemek);
    }
   
    
    console.log(trenutni_uporabnik);

    
    return false;
}


function add_goal() {
    var inputs = document.getElementById("add_goal");
    var opis = inputs[0].value;
    var vrednost = parseInt(inputs[1].value);
    var do_datum = inputs[2].valueAsDate;
    /*
    console.log(opis);
    console.log(vrednost);
    console.log(do_datum);
    */
    var cilj = new Cilj(opis, vrednost, do_datum);
    trenutni_uporabnik.addCilj(cilj);
    
    // dodaj cilj v dropdown
    var goals_dropdown = document.getElementById("goals");
    var option = document.createElement("option");
    option.text = opis;
    option.value = opis;
    goals_dropdown.add(option);
    
    console.log(trenutni_uporabnik);
    
    
    return false;
}


function add_to_goal() {
    var inputs = document.getElementById("add_to_goal");
    var vrednost = parseInt(inputs[0].value);
    var wallet_bank = inputs[1].value;
    var goal = inputs[2].value;
    
    if (vrednost.length == 0) {
        alert("Vnesite vrednost");
        return;
    }
    /*
    console.log(vrednost);
    console.log(wallet_bank);
    console.log(goal);
    */
    
    // dodaj k izbranemu cilju
    var cilj = trenutni_uporabnik.findCilj(goal);
    cilj.povecajTrenutnoPrivarcevano(vrednost);
    
    // odvzemi denar iz denarnice ali banke
    var izdatek_prejemek;
    if (wallet_bank == "wallet") {
        izdatek_prejemek = new IzdatekPrejemek("izdatek", "Dodajanje denarja cilju: " + goal, vrednost, "dodajanje cilju", "denarnica");
        trenutni_uporabnik.denarnica_stanje.addIzdatekPrejemek(izdatek_prejemek);
    }
    else if (wallet_bank == "bank") {
        izdatek_prejemek = new IzdatekPrejemek("izdatek", "Dodajanje denarja cilju: " + goal, vrednost, "dodajanje cilju", "banka");
        trenutni_uporabnik.bancno_stanje.addIzdatekPrejemek(izdatek_prejemek);
    }
    trenutni_uporabnik.executeIzdatekPrejemek(izdatek_prejemek);
        
    console.log(trenutni_uporabnik);
    
    
    return false;
}



function showGoal(elem){
    if(elem.value == "new_goal") { 
        document.getElementsByClassName("new_goals")[0].style.display = "block";
        document.getElementsByClassName("add_data")[0].style.display = "none";
        document.getElementsByClassName("add_to_goal")[0].style.display = "none";
    }
    else if(elem.value == "goal_add_money") { 
        document.getElementsByClassName("add_to_goal")[0].style.display = "block";
        document.getElementsByClassName("add_data")[0].style.display = "none";
        document.getElementsByClassName("new_goals")[0].style.display = "none";
    }
    else {
        document.getElementsByClassName("add_data")[0].style.display = "block";
        document.getElementsByClassName("new_goals")[0].style.display = "none";
        document.getElementsByClassName("add_to_goal")[0].style.display = "none";
    }
}


function showGoal_2(elem){
    if(elem.value == "goals") {
        document.getElementsByClassName("goal_results")[0].style.display = "block";
        document.getElementsByClassName("not_goal_results")[0].style.display = "none";
        document.getElementsByClassName("result_set")[0].style.display = "none";
    }
    else {
        document.getElementsByClassName("not_goal_results")[0].style.display = "block";
        document.getElementsByClassName("result_set")[0].style.display = "block";
        document.getElementsByClassName("goal_results")[0].style.display = "none";
    }
}


function Clicked (button) {
    submit = button ;
}


function find_user_by_username (username) {
    for (var i=0; i<uporabniki.length; i++) {
        if (uporabniki[i].uporabnisko_ime == username) {
            return uporabniki[i];
        }
    }
    return "Ni uporabnika s takim uporabniškim imenom.";
}





/*
window.addEventListener("beforeunload", onCheckLeave);

function onCheckLeave (ev) {
    var inputs = document.querySelectorAll("input[type='text'], input[type='password']");
    
    for (var i=0; i<inputs.length; i++) {
        if (inputs[i].value != "") {
            ev.returnValue = "pozor";
            return "pozor";
        }
    }
}
*/