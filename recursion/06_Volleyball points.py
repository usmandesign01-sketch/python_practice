def volleyball(points):
    if points == 16:
        print("Game Over")
        return

    print("Volleyball point now:",points)
    volleyball(points + 1)

volleyball(0)
