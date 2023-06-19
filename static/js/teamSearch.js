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

// Add an event listener to the League dropdown
document.getElementById("league").addEventListener("change", fetchTeams);

// Call the populateLeaguesDropdown function when the page loads
console.log("Page loaded. Populating leagues dropdown...");
populateLeaguesDropdown();

// Set the current year as the default value for the Season dropdown
var currentYear = new Date().getFullYear();
document.getElementById("season").value = currentYear;

function displayNextFixture(nextFixture) {
    var nextFixtureElement = document.getElementById("next-fixture");
    nextFixtureElement.innerHTML = ""; // Clear the previous content

    if (nextFixture.length > 0) {
        var fixture = nextFixture[0];
        var fixtureHtml = `
            <h3>Next Fixture</h3>
            <p>Home Team: ${fixture.home_team}</p>
            <p>Away Team: ${fixture.away_team}</p>
            <p>Date: ${fixture.date}</p>
            <p>Status: ${fixture.status}</p>
            <p>Score: ${fixture.score}</p>
        `;
        nextFixtureElement.innerHTML = fixtureHtml;
    } else {
        nextFixtureElement.innerHTML = "<p>No next fixture found.</p>";
    }
}

function getNextFixture() {
    console.log("Getting next fixture...");
    var season = document.getElementById("season").value;
    var teamId = document.getElementById("team").value;
    var leagueId = document.getElementById("league").value;

    var xhr = new XMLHttpRequest();
    xhr.open("GET", `/get_next_fixture?season=${season}&team_id=${teamId}&league_id=${leagueId}`, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log("Next fixture fetched successfully.");
                var nextFixture = JSON.parse(xhr.responseText);
                displayNextFixture(nextFixture);
            } else {
                console.error("Error fetching next fixture:", xhr.status);
            }
        }
    };
    xhr.send();
}

function schedulePost() {
    console.log("Scheduling post...");
    var season = document.getElementById("season").value;
    var teamId = document.getElementById("team").value;
    var leagueId = document.getElementById("league").value;

    var data = {
        season: season,
        teamId: teamId,
        leagueId: leagueId
    };

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/schedule_post", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log("Post scheduled successfully.");
                var result = xhr.responseText;
                alert(result);
            } else {
                console.error("Error scheduling post:", xhr.status);
            }
        }
    };
    xhr.send(JSON.stringify(data));
}