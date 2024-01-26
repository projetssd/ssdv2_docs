# Comment configurer les formats personnalisés de langue

Ici, nous expliquerons comment configurer votre propre format personnalisé de langue préférée, avec quelques exemples.

!!! avertissement "L'utilisation des formats personnalisés de langue n'est pas compatible avec la définition d'une langue préférée dans un profil de qualité dans Radarr. Vous devez utiliser l'un ou l'autre.<br>Si vous souhaitez utiliser les formats personnalisés, définissez la langue préférée sur "Toute". .<br><br>Sonarr n'a pas de langue préférée dans le profil de qualité, cela peut donc être ignoré si vous le configurez avec Sonarr"

## Exemples de langage

Importez le JSON dans vos formats personnalisés.

Comment ?

Suivez les instructions [Comment importer des formats personnalisés](/Radarr/Radarr-import-custom-formats/){:target="_blank" rel="noopener noreferrer"}.

---

### Langue : Original uniquement

<sub><sub>Langue : pas d'origine</sub>

C'est l'un des plus couramment utilisés, à part le seul anglais.

Avec ce format personnalisé, vous obtiendrez uniquement le film/émission de télévision dans la langue originale.

Pour cela, nous allons utiliser ce qu'on appelle la notation inversée.

Ajoutez le json suivant à votre Radarr/Sonarr avec un score de « -10000 ».

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/guide-only/langue-not-original.json' %]][[% endfilter %]]
    ```

---

### Langue : anglais uniquement

<sub><sub>Langue : pas l'anglais</sub>

Avec ce format personnalisé, vous obtiendrez uniquement le film/émission de télévision en anglais.

!!! info "Pour les langues autres que l'anglais, remplacez la condition anglaise par la langue de votre choix."

Pour cela, nous allons utiliser ce qu'on appelle la notation inversée.

Ajoutez le json suivant à votre Radarr/Sonarr avec un score de « -10000 ».

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/guide-only/langue-not-english.json' %]][[% endfilter %]]
    ```

---

### Langue : Multiple uniquement

<sub><sub>Langue : pas le néerlandais</sub>

Dans certains cas, vous avez besoin de plusieurs langues dans votre format personnalisé pour différentes raisons.

dans cet exemple, j'utiliserai le néerlandais et le flamand étant donné que de nombreux films/émissions de télévision sont réalisés en collaboration entre les 2 pays/studios.

Avec ce format personnalisé, vous obtiendrez uniquement le film/émission de télévision avec audio néerlandais et/ou flamand.

!!! info "Pour les langues autres que le néerlandais/flamand, remplacez la condition néerlandais/flamand par la langue de votre choix."

Pour cela, nous allons utiliser ce qu'on appelle la notation inversée.

Ajoutez le json suivant à votre Radarr/Sonarr avec un score de « -10000 ».

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/guide-only/langue-not-dutch.json' %]][[% endfilter %]]
    ```

---

### Langue : Je préfère X mais je prendrai Y

<sub><sub>Langue : ni originale ni allemande</sub>
<sub><sub>Langue : Préférer l'allemand</sub>

Disons que vous voulez l'allemand, mais si l'allemand n'est pas disponible, revenez à la langue d'origine mais n'acceptez aucune autre langue traduite.

!!! info "Pour les langues autres que l'allemand, remplacez la condition allemande par la langue de votre choix."

Ajoutez le json suivant à votre Radarr/Sonarr avec un score de « -10000 ».

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/guide-only/langue-not-original-or-german.json' %]][[% endfilter %]]
    ```

Ajoutez le json suivant à votre Radarr/Sonarr avec un score de « 10 ».

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/guide-only/langue-prefer-german.json' %]][[% endfilter %]]
    ```

---

### Langue : Préférer la langue X

<sub><sub>Langue : Préférer l'allemand</sub>

Disons que vous voulez simplement préférer l'allemand et que vous ne vous souciez pas si vous obtenez une ou plusieurs autres langues au hasard.

!!! info "Pour les langues autres que l'allemand, remplacez la condition allemande par la langue de votre choix."

Ajoutez le json suivant à votre Radarr/Sonarr avec un score de « 10 ».

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/guide-only/langue-prefer-german.json' %]][[% endfilter %]]
    ```

---

### Langue : préférez plusieurs langues

<sub><sub>Langue : préférer le néerlandais</sub>

Dans certains cas, vous souhaiterez peut-être préférer plusieurs langues dans votre format personnalisé.

Avec ce format personnalisé, vous n'obtiendrez que le film/l'émission télévisée dans l'une ou l'autre des langues préférées.

Dans cet exemple, j'utiliserai le néerlandais et le flamand pour de nombreux films/émissions de télévision car il y a beaucoup de collaboration entre les deux pays/studios.

!!! info "Pour les langues autres que le néerlandais/flamand, remplacez la condition néerlandais/flamand par la langue de votre choix."

Ajoutez le json suivant à votre Radarr/Sonarr avec un score de « 10 ».

??? exemple "JSON - [Cliquez pour afficher/masquer]"

    ```json
    [[% filter indent(width=4) %]][[% include 'json/guide-only/langue-prefer-dutch.json' %]][[% endfilter %]]
    ```

---

## FAQ et informations

### Qu'est-ce que la notation inversée

??? question "Qu'est-ce que la notation inversée ? - [Cliquez pour afficher/masquer]"

    Avec la notation inversée, vous ajoutez un format personnalisé avec un score de « -10 000 » et vous annulez votre condition préférée.

    Ainsi, dans le cas du format personnalisé suivant « Langue : Original uniquement », il correspondra en fait à toutes les versions non originales et lui donnera un score de « -10 000 ».

### Préférer la langue X à la langue Y

??? question "Préférer la langue X à la langue Y - [Cliquez pour afficher/masquer]"

    Si vous souhaitez préférer Préférer la langue X à la langue Y,

    vous ajoutez par exemple : « Langue : Préférer la langue X » avec un score de « 10 », et ajoutez « Langue : Préférer la langue Y » avec un score de « 9 ».

    Les scores que vous devez utiliser dépendent de l'importance de la langue par rapport aux autres formats personnalisés que vous utilisez.

### Quelle est la langue d'origine

??? question "Quelle est la langue d'origine ? - [Cliquez pour afficher/masquer]"

    La langue originale est la langue dans laquelle un film/une émission de télévision a été initialement réalisé.

### D'où Radarr obtient-il la langue originale

??? question "D'où Radarr obtient-il la langue originale ? - [Cliquez pour afficher/masquer]"

    Radarr utilise [The Movie Database (TMDB)](https://www.themoviedb.org/){:target="_blank" rel="noopener noreferrer"}. Depuis le 12 février 2023, Radarr a mis à jour son cache de métadonnées pour utiliser la langue parlée d'un film de TMDb comme langue d'origine, mais uniquement lorsqu'une seule langue parlée est répertoriée pour ce film sur TMDb. Dans les cas où plusieurs langues parlées sont répertoriées, Radarr utilisera la langue originale désignée du film par TMDb.

    ![!La base de données de films (TMDB) langue originale](images/original-langue-tmdb.png)

### D'où Sonarr obtient-il la langue originale

??? question "D'où Sonarr obtient-il la langue originale ? - [Cliquez pour afficher/masquer]"

    Sonarr utilise [TheTVDB](https://thetvdb.com/){:target="_blank" rel="noopener noreferrer"}.

    ![!Langue originale de TheTVDB](images/original-langue-tvdb.png)

--8<-- "includes/support.md"