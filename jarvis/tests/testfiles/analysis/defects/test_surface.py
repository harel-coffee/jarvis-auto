from jarvis.analysis.defects.surface import wulff_normals, Surface
from jarvis.core.atoms import Atoms


def test_surf():
    box = [[2.715, 2.715, 0], [0, 2.715, 2.715], [2.715, 0, 2.715]]
    coords = [[0, 0, 0], [0.25, 0.25, 0.25]]
    elements = ["Si", "Si"]
    Si = Atoms(lattice_mat=box, coords=coords, elements=elements)
    surface = Surface(atoms=Si, indices=[1, 1, 1])
    s = surface.make_surface()
    # print (s.lattice_mat[0][0])
    td = surface.to_dict()
    fd = Surface.from_dict(td)
    print(fd)
    su = [
        0.8582640971273426,
        0.9334963319196496,
        0.9360461382184894,
        0.9419095687284446,
        0.9802042233627004,
        0.9875446840480956,
        1.0120634294466684,
        1.0126231880823566,
        1.0241538763302507,
        1.0315901848682645,
        1.0318271257831195,
        1.0331286888257398,
        1.0344297141291043,
        1.0388709097092674,
        1.040277640596931,
        1.042494119906149,
        1.04453679643896,
        1.0450598648770613,
        1.045076130339553,
        1.0469310544190567,
        1.0491015867538047,
        1.0495494553198788,
        1.0534717916897114,
        1.0535201391639715,
        1.054233162444997,
        1.0579157863887743,
        1.0595676718662346,
        1.0601381085497692,
        1.109580394178689,
    ]

    ml = [
        [0, 0, 1],
        [2, 0, 3],
        [2, 0, 1],
        [1, 0, 1],
        [3, 0, 2],
        [1, 0, 3],
        [3, 1, 1],
        [3, 0, 1],
        [3, 1, 3],
        [3, -1, 1],
        [3, 1, 0],
        [3, 2, 1],
        [3, 3, 1],
        [1, 0, 0],
        [2, 2, 1],
        [3, -1, 3],
        [3, -1, 2],
        [3, 3, 2],
        [3, 2, 2],
        [2, -1, 3],
        [3, 2, 0],
        [3, 2, 3],
        [1, 1, 1],
        [1, 0, 2],
        [3, 1, 2],
        [2, -1, 2],
        [3, -1, 0],
        [2, 2, 3],
        [1, 1, 0],
    ]
    nm = wulff_normals(miller_indices=ml, surface_energies=su)
    # print (nm)
    tmp = [
        [1.0, [0, 0, 1]],
        [3.921600474095634, [2, 0, 3]],
        [2.438716476826076, [2, 0, 1]],
        [1.552041255230461, [1, 0, 1]],
        [4.117819444608784, [3, 0, 2]],
        [3.638612524088821, [1, 0, 3]],
        [3.910957793469126, [3, 1, 1]],
        [3.7310143772286937, [3, 0, 1]],
        [5.201409757790036, [3, 1, 3]],
        [3.9864158271014745, [3, -1, 1]],
        [3.801771366110844, [3, 1, 0]],
        [4.5039907913791675, [3, 2, 1]],
        [5.2535980512015135, [3, 3, 1]],
        [1.2104326782239008, [1, 0, 0]],
        [3.6362151606205986, [2, 2, 1]],
        [5.294555059585646, [3, -1, 3]],
        [4.553725168318604, [3, -1, 2]],
        [5.711255167942817, [3, 3, 2]],
        [5.020551700372963, [3, 2, 2]],
        [4.564163089568084, [2, -1, 3]],
        [4.407255968031299, [3, 2, 0]],
        [5.735790792628303, [3, 2, 3]],
        [2.1259967341689543, [1, 1, 1]],
        [2.744775943349465, [1, 0, 2]],
        [4.595997097917879, [3, 1, 2]],
        [3.6978680219632056, [2, -1, 2]],
        [3.9039815243280183, [3, -1, 0]],
        [5.092909529739627, [2, 2, 3]],
        [1.8283225958570692, [1, 1, 0]],
    ]
    assert (round(s.lattice_mat[0][0], 2), nm) == (7.68, tmp)


# test_surf()
