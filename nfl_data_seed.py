from app import create_app, db
from app.models import Player

def seed_players():
    app = create_app()

    with app.app_context():
        db.drop_all()
        db.create_all()

        players = [
            # QBs
            Player(full_name="Tom Brady", position="QB", team="NE/TB", seasons=22, games_played=335, total_yards=89000, touchdowns=650, interceptions=210),
            Player(full_name="Peyton Manning", position="QB", team="IND/DEN", seasons=18, games_played=266, total_yards=71000, touchdowns=540, interceptions=250),
            Player(full_name="Drew Brees", position="QB", team="SD/NO", seasons=20, games_played=287, total_yards=80000, touchdowns=570, interceptions=240),
            Player(full_name="Aaron Rodgers", position="QB", team="GB/NYJ", seasons=19, games_played=232, total_yards=59000, touchdowns=475, interceptions=105),
            Player(full_name="Brett Favre", position="QB", team="ATL/GB/NYJ/MIN", seasons=20, games_played=302, total_yards=72000, touchdowns=508, interceptions=336),
            Player(full_name="Patrick Mahomes", position="QB", team="KC", seasons=7, games_played=96, total_yards=28000, touchdowns=220, interceptions=50),
            Player(full_name="Josh Allen", position="QB", team="BUF", seasons=6, games_played=94, total_yards=24000, touchdowns=180, interceptions=70),
            Player(full_name="Joe Burrow", position="QB", team="CIN", seasons=4, games_played=52, total_yards=14000, touchdowns=97, interceptions=37),
            Player(full_name="Matt Ryan", position="QB", team="ATL/IND", seasons=15, games_played=234, total_yards=62000, touchdowns=390, interceptions=180),
            Player(full_name="Matthew Stafford", position="QB", team="DET/LAR", seasons=15, games_played=205, total_yards=53000, touchdowns=340, interceptions=180),
            Player(full_name="Kirk Cousins", position="QB", team="WAS/MIN/ATL", seasons=12, games_played=150, total_yards=38000, touchdowns=270, interceptions=110),
            Player(full_name="Baker Mayfield", position="QB", team="CLE/CAR/LAR/TB", seasons=6, games_played=94, total_yards=16000, touchdowns=102, interceptions=64),
            Player(full_name="Jalen Hurts", position="QB", team="PHI", seasons=4, games_played=62, total_yards=11000, touchdowns=75, interceptions=29),
            Player(full_name="Lamar Jackson", position="QB", team="BAL", seasons=6, games_played=86, total_yards=15000, touchdowns=125, interceptions=45),

            # RBs
            Player(full_name="Emmitt Smith", position="RB", team="DAL/ARI", seasons=15, games_played=226, total_yards=22000, touchdowns=175, interceptions=0),
            Player(full_name="Barry Sanders", position="RB", team="DET", seasons=10, games_played=153, total_yards=18000, touchdowns=109, interceptions=0),
            Player(full_name="Walter Payton", position="RB", team="CHI", seasons=13, games_played=190, total_yards=21000, touchdowns=125, interceptions=0),
            Player(full_name="LaDainian Tomlinson", position="RB", team="SD/NYJ", seasons=11, games_played=170, total_yards=19000, touchdowns=162, interceptions=0),
            Player(full_name="Adrian Peterson", position="RB", team="MIN/WAS/DET/TEN/SEA", seasons=14, games_played=184, total_yards=19000, touchdowns=150, interceptions=0),
            Player(full_name="Derrick Henry", position="RB", team="TEN/BAL", seasons=8, games_played=119, total_yards=12000, touchdowns=93, interceptions=0),
            Player(full_name="Christian McCaffrey", position="RB", team="CAR/SF", seasons=7, games_played=91, total_yards=11000, touchdowns=85, interceptions=0),
            Player(full_name="Saquon Barkley", position="RB", team="NYG/PHI", seasons=6, games_played=75, total_yards=7000, touchdowns=50, interceptions=0),
            Player(full_name="Marshawn Lynch", position="RB", team="BUF/SEA/OAK", seasons=12, games_played=149, total_yards=10500, touchdowns=94, interceptions=0),
            Player(full_name="Frank Gore", position="RB", team="SF/IND/MIA/BUF/NYJ", seasons=16, games_played=241, total_yards=20000, touchdowns=100, interceptions=0),
            Player(full_name="Ezekiel Elliott", position="RB", team="DAL/NE", seasons=8, games_played=118, total_yards=10000, touchdowns=73, interceptions=0),
            Player(full_name="Nick Chubb", position="RB", team="CLE", seasons=6, games_played=77, total_yards=9000, touchdowns=55, interceptions=0),

            # WRs
            Player(full_name="Jerry Rice", position="WR", team="SF/OAK/SEA", seasons=20, games_played=303, total_yards=23000, touchdowns=208, interceptions=0),
            Player(full_name="Randy Moss", position="WR", team="MIN/OAK/NE/TEN/SF", seasons=14, games_played=218, total_yards=17000, touchdowns=163, interceptions=0),
            Player(full_name="Terrell Owens", position="WR", team="SF/PHI/DAL/BUF/CIN", seasons=15, games_played=219, total_yards=16000, touchdowns=153, interceptions=0),
            Player(full_name="Larry Fitzgerald", position="WR", team="ARI", seasons=17, games_played=263, total_yards=17000, touchdowns=121, interceptions=0),
            Player(full_name="Calvin Johnson", position="WR", team="DET", seasons=9, games_played=135, total_yards=11600, touchdowns=83, interceptions=0),
            Player(full_name="DeAndre Hopkins", position="WR", team="HOU/ARI/TEN", seasons=11, games_played=148, total_yards=12000, touchdowns=80, interceptions=0),
            Player(full_name="Davante Adams", position="WR", team="GB/LV", seasons=10, games_played=137, total_yards=11000, touchdowns=90, interceptions=0),
            Player(full_name="Tyreek Hill", position="WR", team="KC/MIA", seasons=8, games_played=121, total_yards=10000, touchdowns=80, interceptions=0),
            Player(full_name="Odell Beckham Jr.", position="WR", team="NYG/CLE/LAR/BAL", seasons=10, games_played=110, total_yards=8500, touchdowns=60, interceptions=0),
            Player(full_name="Mike Evans", position="WR", team="TB", seasons=10, games_played=150, total_yards=11000, touchdowns=90, interceptions=0),
            Player(full_name="Stefon Diggs", position="WR", team="MIN/BUF", seasons=9, games_played=131, total_yards=9000, touchdowns=60, interceptions=0),

            # TEs
            Player(full_name="Travis Kelce", position="TE", team="KC", seasons=11, games_played=159, total_yards=11000, touchdowns=75, interceptions=0),
            Player(full_name="Rob Gronkowski", position="TE", team="NE/TB", seasons=11, games_played=143, total_yards=9500, touchdowns=92, interceptions=0),
            Player(full_name="Tony Gonzalez", position="TE", team="KC/ATL", seasons=17, games_played=270, total_yards=15000, touchdowns=111, interceptions=0),
            Player(full_name="Antonio Gates", position="TE", team="LAC", seasons=16, games_played=236, total_yards=12000, touchdowns=116, interceptions=0),
            Player(full_name="George Kittle", position="TE", team="SF", seasons=7, games_played=84, total_yards=6000, touchdowns=35, interceptions=0),

            # DL / LB
            Player(full_name="Michael Strahan", position="DE", team="NYG", seasons=15, games_played=216, total_yards=800, touchdowns=5, interceptions=0),
            Player(full_name="Reggie White", position="DE", team="PHI/GB/CAR", seasons=15, games_played=232, total_yards=900, touchdowns=10, interceptions=0),
            Player(full_name="J.J. Watt", position="DE", team="HOU/ARI", seasons=12, games_played=151, total_yards=850, touchdowns=7, interceptions=0),
            Player(full_name="Aaron Donald", position="DT", team="LAR", seasons=10, games_played=154, total_yards=700, touchdowns=2, interceptions=0),
            Player(full_name="Ray Lewis", position="LB", team="BAL", seasons=17, games_played=228, total_yards=1200, touchdowns=41, interceptions=30),
            Player(full_name="Brian Urlacher", position="LB", team="CHI", seasons=13, games_played=182, total_yards=1000, touchdowns=22, interceptions=20),
            Player(full_name="Luke Kuechly", position="LB", team="CAR", seasons=8, games_played=118, total_yards=900, touchdowns=15, interceptions=18),
            Player(full_name="T.J. Watt", position="LB", team="PIT", seasons=8, games_played=104, total_yards=600, touchdowns=8, interceptions=7),

            # DBs
            Player(full_name="Ed Reed", position="S", team="BAL/HOU/NYJ", seasons=12, games_played=174, total_yards=500, touchdowns=13, interceptions=64),
            Player(full_name="Troy Polamalu", position="S", team="PIT", seasons=12, games_played=158, total_yards=300, touchdowns=3, interceptions=32),
            Player(full_name="Earl Thomas", position="S", team="SEA/BAL", seasons=9, games_played=140, total_yards=250, touchdowns=3, interceptions=30),
            Player(full_name="Deion Sanders", position="CB", team="ATL/SF/DAL/WAS/BAL", seasons=14, games_played=188, total_yards=500, touchdowns=22, interceptions=53),
            Player(full_name="Darrelle Revis", position="CB", team="NYJ/TB/NE/KC", seasons=11, games_played=145, total_yards=200, touchdowns=3, interceptions=30),
            Player(full_name="Richard Sherman", position="CB", team="SEA/SF/TB", seasons=11, games_played=144, total_yards=300, touchdowns=3, interceptions=37),

            # Kickers
            Player(full_name="Justin Tucker", position="K", team="BAL", seasons=12, games_played=194, total_yards=50, touchdowns=0, interceptions=0),
            Player(full_name="Adam Vinatieri", position="K", team="NE/IND", seasons=24, games_played=365, total_yards=80, touchdowns=0, interceptions=0),
        ]

        db.session.add_all(players)
        db.session.commit()
        print(f"Seeded {len(players)} players.")

if __name__ == "__main__":
    seed_players()
