import pstats

paths = ["manage.prof", "registration/reg_views.prof", "vnos/vnos_views.prof", "pregled/pregled_views.prof", "vizualizacija/vizualizacija_views.prof"]

def print_stats(paths):
    for path in paths:
        p = pstats.Stats(path)
        p.sort_stats('cumulative').print_stats(10)
        print("\n\n\n")


print_stats(paths)