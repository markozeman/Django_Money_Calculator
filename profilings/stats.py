import pstats

paths = ["profilings/manage.prof", "profilings/reg_views.prof", "profilings/vnos_views.prof", "profilings/pregled_views.prof", "profilings/vizualizacija_views.prof"]

def print_stats(paths):
    for path in paths:
        p = pstats.Stats(path)
        p.sort_stats('cumulative').print_stats(10)
        print("\n\n\n")

print_stats(paths)