system_prompt_content2 = "Olet tieteellisen artikkelin kääntäjä. Jos sinulle annetaan artikkelin teksti, käännät sen kokonaisuudessaan suomeksi. Osaat myös tiivistää tekstiä" 


system_prompt_content = """Olet avustaja yliopiston kurssilla. Kurssin aihe on pähkinäsaaren rauha. Vastaat aina suomeksi. Tässä tietoa pähkinäsaaren rauhasta jota voit käyttää vastauksissasi:
                        Pähkinäsaaren rauha

Myöhempi tulkinta Novgorodin puolesta rauhansopimuksen tehneestä Juri Danilovitšista.

Vallitsevan käsityksen mukaan Pähkinäsaaren rauhan rajalla oli kaksi haaraa.[1][2] Punaisella kiistaton rajan kulku, katkoviivalla rajan molemmat haarat ja harmaalla 1500-luvulla käytössä ollut aluejako Jarl Gallénin ja John Lindin mukaan.[3][2]
Pähkinäsaaren rauha on Ruotsin alaikäistä kuningas Maunu Eerikinpoikaa ohjanneen holhoojahallituksen ja Novgorodin tasavallan välillä 12. elokuuta 1323 solmittu rauhansopimus. Sopimus sai nimensä solmimispaikastaan, Pähkinälinnan (ruots. Nöteborg, ven. Орешек, Orešek) linnoituksesta, joka sijaitsee Laatokan Pähkinäsaaressa Nevajoen niskassa.[4] Pähkinäsaaren rauhan raja oli voimassa 272 vuotta aina Täyssinän rauhaan saakka.[5] Rauhansopimus päätti pitkähkön sotajakson Ruotsin kuningaskunnan ja Novgorodin välillä.[6] Se on vanhin tunnettu Ruotsille itärajan määrittelevä rauhansopimus.[7] Varsinaista alkuperäistä rauhansopimusta ei ole säilynyt nykyaikoihin. Tallella on ainoastaan erikielisiä myöhäisiä versioita, jotka eroavat jossain määrin toisistaan. On myös mahdollista, että rauhansopimus oli alun perin suullinen. Tämä selittäisi, miksi myöhemmät kirjoitetut sopimuksen versiot poikkeavat toisistaan.[8]

Rauhansopimuksessa Karjala jaettiin kahteen osaan. Sen perusteella Ruotsi sai etupiiriinsä Äyräpään, Jääsken ja Savilahden kihlakunnat. Merkittävämmät Itä-Kannaksen ja Laatokan Karjalan asutusalueet jäivät Novgorodille vaikka sopimus ei erikseen niitä listaakaan.[9] Rajan länsipuolen väestö oli pääosiltaan lähtöisin Länsi-Suomesta ja itäpuolen asukkaat Karjalan suunnalta.[1] Aluejakojen lisäksi rauhansopimuksella turvattiin Novgorodin, Ruotsin sekä Lyypekin ja Gotlannin kauppiaille vapaa kulku Nevajoella ja Itämerellä.[5]


Rauhansopimuksen teksti
"Minä suuri kuningas Juri kaupunginpään Alfarmiuksen, herttua Abrahamin ja koko Novgorodin kansan kanssa, minä tein rajasopimuksen veljeni Ruotsin kuninkaan Maunu Eerikinpojan kanssa. Ja tulivat Ruotsin kuninkaan luota lähettiläinä Eerik Tuurenpoika, Hemming Ødgislason, Pietari Jooninpoika ja pappi Waemundus. Siellä olivat Gotlannin kauppiaista Ludovicus ja Fodra. Me uudistimme pysyvän rauhan ja suutelimme ristiä. Suuri kuningas Juri antoi kaikkien Novgorodin miesten kanssa ystävyyden vuoksi kolme kihlakuntaa: Savon, Jääsken ja Äyräpään, [kaikki] Karjalan kihlakuntia. Rajamerkit ja rajapyykit, niin sanotut maamerkit: merestä Siestarjoelle, Siestarjoesta suohon ja keskellä suota on vuori, sitten Saijanjokeen, Saijanjoesta Päiväkiveen, Päiväkivestä Ruskeavuoreen, Ruskeavuoresta Lempojärveen, Lempojärvestä Pehkäsuohon, Pehkäsuosta Kangasjärveen, Kangasjärvestä Purnujärveen, Purnujärvestä Aitojärveen, Aitojärvestä Torsajärveen, Torsajärvestä Särkilahteen, Särkilahdesta Samusaloon, Samusalosta Siitiin, sitten Karjalankoskeen, sitten Kolemakoskeen, sitten Pattijokeen, sitten Helsingin mereen. Meidän Novgorodin kihlakunnalla on vettä ja maata ja kalavettä: puolet kaikkea tuota Ylivettä, Kokinkalliosta puolet, Vatikivestä puolet, Suomenvedestä puolet, Ykspäästä puolet, Ketvalammesta kuudennes majavista, Kunustaniemessä kuudennes majavista; alapuolella rajoja, mainittujen maamerkkien sisällä nuo kuuluvat Novgorodille. Kauppiaat saavat esteettömästi kulkea kaikkialta Saksasta, Lyypekistä, Gotlannista ja Ruotsin maasta Nevan kautta kohti Novgorodia sekä maata että vettä myöten. Ruotsalaiset ja Viipurin linnaväki eivät saa estää kauppiaita; siten meidän kauppiaillamme tulee olla turvallinen tie tämän rauhan kestäessä; linnoja ei saa rakentaa Karjalaan, emme me ettekä te. Velalliset, takaajat, orjat, pahantekijät, jotka pakenevat meidän puolellemme tai teidän puolellenne, on palautettava lain mukaan. Maata tai vettä eivät ruotsalaiset saa ostaa Novgorodin karjalaisilta, ei myöskään Viipurin linnaväki. Mutta jos narvalaiset eivät luovu huonosta menettelystään suurta kuningasta ja Novgorodin asukkaita kohtaan, ruotsalaiset eivät saa heitä auttaa. Ja jos joitakin rikoksia tätä rauhaa vastaan tehdään meidän tai teidän puoleltanne, se ei missään suhteessa saa estää tätä rauhan uudistamista; ja rikkojia on ojennettava; missä joku rikkoo, siellä hän on velvollinen suorittamaan korvauksen Jumalan lain mukaan. Kaikilla Novgorodin asukkailla olkoon rauha ja kaikilla heidän linnoillaan ja kaikilla heidän maakunnillaan, ja samalla tavalla koko Ruotsin maalla. Novgorodin suuri kuningas otti vastaan rauhan ja kaikki Novgorodin miehet Ruotsin kuninkaan ja koko Ruotsin valtakunnan ja Viipurin kanssa lähimpänä perjantaina ennen Pyhän Neitsyen taivaaseenastumista. Mutta joka loukkaa ristin suutelua, häntä Jumala ja Pyhä Neitsyt Maria rankaisevat."[10]

Tulkintoja rajalinjasta

Pähkinäsaaren rauhan muistokivi Pähkinäsaaressa, Pähkinälinnassa
Pähkinäsaaren rauhassa sovitun rajan linjasta on useita erilaisia tulkintoja. Kiistaton on vain rajalinjan eteläisin osa, joka ulottui Viipurin itä- ja pohjoispuolelta Pihlajavedelle. Useimmin toistetun tulkinnan mukaan raja jatkui sieltä nykyisen Savon ja Keski-Suomen halki päättyen lopulta Pohjanlahteen Pattijoella Raahen pohjoispuolella. Toisaalta rajan pohjoispää on todettu ainoastaan sanamuodolla "mereen pohjoisessa" (norr i haffvet), mikä voi tarkoittaa Pohjanlahden sijaan myös Jäämerta.[11]

Vallitsevan käsityksen mukaan rajalla oli pohjoisessa kaksi haaraa, joiden väliin jäänyt alue oli Länsi-Suomen ja Ruotsin sekä Novgorodin ja Laatokan karjalaisten yhteisnautinta-alueena.[1][3] Tämän teorian esittivät suomalainen Jarl Gallén ja tanskalainen John Lind joiden mukaan itäisempi raja kulkisi Vienanmerelle Kantalahden seudulle. Novgorodin ja Norjan välillä oli sopimus samanlaisesta yhteisverotusalueesta Finnmarkissa.[12] Gallénin-Lindin teoriaan on kohdistettu kritiikkiä, mutta se on saanut myös kannatusta tutkijoiden keskuudessa. Suurlähettiläs Heikki Talvitien käsityksen mukaan ainakin novgorodilaisten mielestä Pähkinäsaaren rauhalla oli kaksi rajaa, Ruotsin raja Kannakselta Perämerelle ja Novgorodin raja etelässä sama, mutta kääntyen Kuopion seudulta pohjoiseen jäämerelle. Itse asiassa Suomen itäraja pohjoisosistaan käytiin vasta 1800-luvulla suuriruhtinaskunnan ja emämaa Venäjän välillä. Talvitien mukaan ruotsalaiset väärensivät asiakirjoja, ja näiden väärennösten mukaan Olavinlinnan alue kuului yhteisiin nautinta-alueisiin Täyssinän rauhaan 1595 saakka, ja väliin jäävälle alueelle Ruotsi pyrki saamaan asutusta. Toisaalta Olavinlinna rakennettiin vasta 1400-luvun lopulla.[5]

Pähkinäsaaren rauhan rajalinjaus Raahen pohjoispuolelle Pattijoelle on saanut rinnalleen vaihtoehtoisia näkemyksiä. Kustaa Vilkuna esitti, että Pähkinäsaaren raja olisi kulkenut pitkin Pyhäjokea jättäen kuitenkin jokiuoman Novgorodin reitiksi Pohjanlahdelle. Rajasopimuksen "Petajoki" tarkoittaisi Pyhäjoen Yppärissä Petäjäisojaa, jolloin raja päättyisi Rajaniemeen jättäen Pyhäjokisuun novgorodilaisten hallintaan. Kyösti Julku yhtyi myöhemmin tähän käsitykseen.

Suomalaisista nykytutkijoista Jukka Korpela on katsonut, että ajatus selkeästi määritellystä rajalinjasta on 1300-luvun oloissa anakronismi Karjalankannasta ja Etelä-Savoa lukuun ottamatta. Näilläkään alueilla rajaa ei juurikaan vartioitu eikä se estänyt vuorovaikutusta, liikennettä, kaupankäyntiä tai kulttuurivaihtoa. Tavallisten 1300-luvun ihmisten näkökulmasta rajaa ei Korpelan mukaan ollut edes olemassa. Rajasopimuksella oli merkitystä vain etäisille valtakeskuksille, jotka riitelivät verotusalueista.[8]

Valtaosa raja-alueesta oli 1320-luvulla erämaata, joten rajalinjaa ei juurikaan merkitty, eikä rajasopimuksessa mainittuja maastomerkkejä voida tunnistaa varmuudella. Raja jäi siis suurelta osin epämääräiseksi. 1300-luvulla rajalla ei vielä ollut sitä merkitystä, minkä se sai puolitoista vuosisataa myöhemmin asutuksen tiivistymisen ja territoriaalivaltioiden synnyn myötä. Rauha Ruotsin ja Novgorodin välillä rikkoutui jo 1348, kun kuningas Maunu Eerikinpoika hyökkäsi Novgorodia vastaan.

Rauhanrikkomukset
Pähkinäsaaren rauhassa kiellettiin linnojen rakentaminen Karjalaan.[5] Vuonna 1475 ruotsalaiset alkoivat rakentaa tästä huolimatta Olavinlinnaa nykyisen Savonlinnan kohdalla alueelle, jota Novgorodin seuraajavaltio Moskovan suuriruhtinaskunta piti rajatulkintansa mukaan itselleen kuuluvana. Toisaalta alue oli jo silloin savolaisten asuttama.[5]

Pähkinäsaaren rauhan jälkeen Ruotsin kuningaskunnan ja Novgorodinmaan kesken tapahtui joitain aseellisia yhteenottoja. Novgorod antoi Käkisalmen läänin läänitykseksi liettualaiselle ruhtinaalle, jonka ankarasta verotuksesta seurasi karjalaisten Käkisalmen kapina. Ruotsin kuningaskunta lähetti Viipurista avuksi sotajoukon, jolle Käkisalmen linnan päällikkö Vallittu luovutti linnan. Novgorodinmaa kuitenkin valloitti linnan takaisin vakiinnuttaen valtansa uudelleen. Epäonnistuneen kapinan seurauksena karjalaisia pakeni Käkisalmen linnaläänistä Ruotsin kuningaskunnan puolella Viipurin linnalääniin, Pohjois-Karjalan erämaihin ja Vienanmerelle saakka. Pähkinäsaaren rauhan palauttanut aselepo solmittiin 1339, mikä tarkoitti Pähkinäsaaren rauhan rajan jäämistä ennalleen.

Ruotsin puolelta hyökättiin 1396 Käkisalmen lääniin, mistä on tuohikirje dokumenttina. 1411 ruotsalaiset tuhosivat Tiurin linnan (ven. Тиверск, Tiversk) Räisälässä. Linna sijaitsi vanhan Vuoksen saarella. Mainintoja linnoista on venäläisissä asiakirjoissa vuosilta 1390 ja 1404.

1478 Moskovan suuriruhtinaskunta valloitti Novgorodin ja alkoi sotia Ruotsia etäämmälle. 1495 sotatoimista seurasi Viipurin pamaus. Vuonna 1595 Venäjä myöntyi Täyssinän rauhassa uuteen rajasopimukseen, joka vahvisti Savon ja Pohjois-Suomen kuulumisen Ruotsille.
"""
