// Function to populate the League dropdown with the predefined leagues
function populateLeaguesDropdown() {
    var leagueDropdown = document.getElementById("league");
    var leagues = [
        { id: 8, name: "Womens WC" },
        { id: 1, name: "1. Bundesliga" },
        { id: 2, name: "2. Bundesliga" },
        { id: 3, name: "3. Bundesliga" },
        { id: 4, name: "DFB-Pokal" },
        { id: 5, name: "UEFA Champions League" },
        { id: 6, name: "Europa League" }
    ];
    leagues.forEach(function(league) {
        var option = document.createElement("option");
        option.value = league.id;
        option.text = league.name;
        leagueDropdown.appendChild(option);
    });
}

// Call the populateLeaguesDropdown function when the page loads
console.log("Page loaded. Populating leagues dropdown...");
populateLeaguesDropdown();

// Function to fetch the list of teams for the selected league and season
function fetchTeams() {
    console.log("Fetching teams...");
    var season = document.getElementById("season").value;
    var leagueId = document.getElementById("league").value;

    var xhr = new XMLHttpRequest();
    xhr.open("GET", `/teams?season=${season}&leagueId=${leagueId}`, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log("Teams fetched successfully.");
                var teams = JSON.parse(xhr.responseText);
                populateTeamsDropdown(teams);
            } else {
                console.error("Error fetching teams:", xhr.status);
            }
        }
    };
    xhr.send();
}

// Add an event listener to the League dropdown
document.getElementById("league").addEventListener("change", fetchTeams);

// Call the populateLeaguesDropdown function when the page loads
console.log("Page loaded. Populating leagues dropdown...");
populateLeaguesDropdown();

// Set the current year as the default value for the Season dropdown
var currentYear = new Date().getFullYear();
document.getElementById("season").value = currentYear;

function displayNextFixtures(nextFixtures) {
    var nextFixturesElement = document.getElementById("next-fixtures");
    nextFixturesElement.innerHTML = ""; // Clear the previous content

    if (nextFixtures.length > 0) {
        var table = document.createElement("table");
        table.classList.add("table");
        var thead = document.createElement("thead");
        var tbody = document.createElement("tbody");

        // Create table header
        var headerRow = document.createElement("tr");
        var headers = ["Home Team", "Away Team", "Date", "Status", "Score"];
        headers.forEach(function(header) {
            var th = document.createElement("th");
            th.textContent = header;
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);
        table.appendChild(thead);

        // Create table rows
        nextFixtures.forEach(function(fixture) {
            var row = document.createElement("tr");
            var columns = [
                fixture.home_team,
                fixture.away_team,
                fixture.date,
                fixture.status,
                fixture.score
            ];
            columns.forEach(function(column) {
                var td = document.createElement("td");
                td.textContent = column;
                row.appendChild(td);
            });
            tbody.appendChild(row);
        });
        table.appendChild(tbody);

        nextFixturesElement.appendChild(table);
    } else {
        nextFixturesElement.innerHTML = "<p>No next fixtures found.</p>";
    }
}

function getNextFixtures() {
    console.log("Getting next fixtures...");
    var season = document.getElementById("season").value;
    var teamId = document.getElementById("team").value;
    var leagueId = document.getElementById("league").value;

    var xhr = new XMLHttpRequest();
    xhr.open("GET", `/get_next_fixture?season=${season}&team_id=${teamId}&league_id=${leagueId}`, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log("Next fixtures fetched successfully.");
                var nextFixtures = JSON.parse(xhr.responseText);
                displayNextFixtures(nextFixtures);
            } else {
                console.error("Error fetching next fixtures:", xhr.status);
            }
        }
    };
    xhr.send();
}

// Function to populate the Team dropdown with the retrieved data
function populateTeamsDropdown(teams) {
    console.log("Populating teams dropdown...");
    var teamDropdown = document.getElementById("team");
    teamDropdown.innerHTML = ""; // Clear the dropdown before populating
    teams.forEach(function(team) {
        var option = document.createElement("option");
        option.value = team.id;
        option.text = team.name;
        teamDropdown.appendChild(option);
    });
    teamDropdown.disabled = false; // Enable the Team dropdown
}