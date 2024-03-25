def TestTimeConsuming():
    from sankethchebbi.truss import Truss

    # Global variables
    TEST_FILE_NUMBER = 47
    TEST_LOAD_CASE   = 0
    TEST_INPUT_FILE  = f"./data/bar-{TEST_FILE_NUMBER}_input_{TEST_LOAD_CASE}.json"
    TRUSS_DIMENSION  = 2
    TEST_TIME_NUMBER = 30

    # Truss object and read .json:
    truss = Truss(dim=TRUSS_DIMENSION)
    truss.LoadFromJSON(TEST_INPUT_FILE)

    # Do direct stiffness method:
    import time
    ts = []
    for _ in range(TEST_TIME_NUMBER):
        t0 = time.time()
        truss.Solve()
        ts.append(time.time() - t0)

    mean = sum(ts) / len(ts)
    print(f"Time for structural analysis = {mean}(s)")
    return mean


def TestPlot():
    from sankethchebbi.truss import Truss
    from sankethchebbi.plot  import TrussPlotter

    # Global variables
    TEST_FILE_NUMBER        = 10
    TEST_LOAD_CASE          = 0
    TEST_INPUT_FILE         = f"./data/bar-{TEST_FILE_NUMBER}_output_{TEST_LOAD_CASE}.json"
    TEST_PLOT_SAVE_PATH     = f"./plot/bar-{TEST_FILE_NUMBER}_plot_{TEST_LOAD_CASE}.png"
    TRUSS_DIMENSION         = 2
    IS_EQUAL_AXIS           = True
    IS_PLOT_STRESS          = True
    IS_SAVE_PLOT            = False
    MAX_SCALED_DISPLACEMENT = 2
    MAX_SCALED_FORCE        = 100
    POINT_SIZE_SCALE_FACTOR = 1
    ARROW_SIZE_SCALE_FACTOR = 1

    # Truss object:
    truss = Truss(dim=TRUSS_DIMENSION)

    # You could directly read the output .json file.
    truss.LoadFromJSON(TEST_INPUT_FILE, isOutputFile=True)

    # Show or save the structural analysis result figure:
    TrussPlotter(truss,
                 isEqualAxis=IS_EQUAL_AXIS,
                 isPlotStress=IS_PLOT_STRESS,
                 maxScaledDisplace=MAX_SCALED_DISPLACEMENT,
                 maxScaledForce=MAX_SCALED_FORCE,
                 pointScale=POINT_SIZE_SCALE_FACTOR,
                 arrowScale=ARROW_SIZE_SCALE_FACTOR).Plot(IS_SAVE_PLOT, TEST_PLOT_SAVE_PATH)


def TestExample():
    from sankethchebbi.truss import Truss
    from sankethchebbi.type  import SupportType, MemberType
    from sankethchebbi.plot  import TrussPlotter

    # -------------------- Global variables --------------------
    # Files settings:
    TEST_OUTPUT_FILE        = f"./test_output.json"
    TEST_PLOT_SAVE_PATH     = f"./test_plot.png"

    # Some settings:
    TRUSS_DIMENSION         = 3
    IS_PLOT_TRUSS           = True
    IS_SAVE_PLOT            = False

    # Plot layout settings:
    IS_EQUAL_AXIS           = True    # Whether to use actual aspect ratio in the truss figure or not.
    MAX_SCALED_DISPLACEMENT = 30      # Scale the max value of all dimensions of displacements.
    MAX_SCALED_FORCE        = 100     # Scale the max value of all dimensions of force arrows.
    POINT_SIZE_SCALE_FACTOR = 1       # Scale the default size of joint point in the truss figure.
    ARROW_SIZE_SCALE_FACTOR = 1       # Scale the default size of force arrow in the truss figure.
    # ----------------------------------------------------------

    # Truss object:
    truss = Truss(dim=TRUSS_DIMENSION)

    # Read data in this [.py]:
    joints     = [(0, 0, 0), (360, 0, 0), (360, 180, 0), (0, 200, 0), (120, 100, 180)]
    supports   = [SupportType.PIN, SupportType.ROLLER_Z, SupportType.PIN, SupportType.PIN, SupportType.NO]
    forces     = [(1, (0, -10000, 5000))]
    members    = [(0, 4), (1, 4), (2, 4), (3, 4), (1, 2), (1, 3)]
    memberType = MemberType(1, 1e7, 1)

    for joint, support in zip(joints, supports):
        truss.AddNewJoint(joint, support)

    for jointID, force in forces:
        truss.AddExternalForce(jointID, force)

    for jointID0, jointID1 in members:
        truss.AddNewMember(jointID0, jointID1, memberType)

    # Do direct stiffness method:
    truss.Solve()

    # Dump all the structural analysis results into a .json file:
    truss.DumpIntoJSON(TEST_OUTPUT_FILE)

    # Show or save the structural analysis result figure:
    if IS_PLOT_TRUSS:
        TrussPlotter(truss,
                     isEqualAxis=IS_EQUAL_AXIS,
                     maxScaledDisplace=MAX_SCALED_DISPLACEMENT,
                     maxScaledForce=MAX_SCALED_FORCE,
                     pointScale=POINT_SIZE_SCALE_FACTOR,
                     arrowScale=ARROW_SIZE_SCALE_FACTOR).Plot(IS_SAVE_PLOT, TEST_PLOT_SAVE_PATH)

    # Get result of structural analysis:
    displace, stress, resistance = truss.GetDisplacements(), truss.GetInternalStresses(), truss.GetResistances()
    return displace, stress, resistance


def TestLoadFromJSON():
    from sankethchebbi.truss import Truss
    from sankethchebbi.plot  import TrussPlotter

    # -------------------- Global variables --------------------
    # Files settings:
    TEST_FILE_NUMBER        = 10
    TEST_LOAD_CASE          = 0
    TEST_INPUT_FILE         = f"./data/bar-{TEST_FILE_NUMBER}_input_{TEST_LOAD_CASE}.json"
    TEST_OUTPUT_FILE        = f"./data/bar-{TEST_FILE_NUMBER}_output_{TEST_LOAD_CASE}.json"
    TEST_PLOT_SAVE_PATH     = f"./plot/bar-{TEST_FILE_NUMBER}_plot_{TEST_LOAD_CASE}.png"

    # Some settings:
    TRUSS_DIMENSION         = 2
    IS_PLOT_TRUSS           = True
    IS_SAVE_PLOT            = False

    # Plot layout settings:
    IS_EQUAL_AXIS           = True   # Whether to use actual aspect ratio in the truss figure or not.
    MAX_SCALED_DISPLACEMENT = 10     # Scale the max value of all dimensions of displacements.
    MAX_SCALED_FORCE        = 50     # Scale the max value of all dimensions of force arrows.
    POINT_SIZE_SCALE_FACTOR = 1      # Scale the default size of joint point in the truss figure.
    ARROW_SIZE_SCALE_FACTOR = 1      # Scale the default size of force arrow in the truss figure.
    # ----------------------------------------------------------

    # Truss object:
    truss = Truss(dim=TRUSS_DIMENSION)

    # Read data in [.json]:
    truss.LoadFromJSON(TEST_INPUT_FILE)

    # Do direct stiffness method:
    truss.Solve()

    # Dump all the structural analysis results into a .json file:
    truss.DumpIntoJSON(TEST_OUTPUT_FILE)

    # Show or save the structural analysis result figure:
    if IS_PLOT_TRUSS:
        TrussPlotter(truss,
                     isEqualAxis=IS_EQUAL_AXIS,
                     maxScaledDisplace=MAX_SCALED_DISPLACEMENT,
                     maxScaledForce=MAX_SCALED_FORCE,
                     pointScale=POINT_SIZE_SCALE_FACTOR,
                     arrowScale=ARROW_SIZE_SCALE_FACTOR).Plot(IS_SAVE_PLOT, TEST_PLOT_SAVE_PATH)

    # Get result of structural analysis:
    displace, stress, resistance = truss.GetDisplacements(), truss.GetInternalStresses(), truss.GetResistances()
    return displace, stress, resistance


def TestGA():
    from sankethchebbi.truss import Truss
    from sankethchebbi.type  import MemberType
    from sankethchebbi.ga    import GA
    import random

    # Allowable stress and displacement:
    ALLOWABLE_STRESS         = 30000.
    ALLOWABLE_DISPLACEMENT   = 10.

    # Type the member types you want to use here:
    MEMBER_TYPE_LIST = [MemberType(inch, random.uniform(1e7, 3e7), random.uniform(0.1, 1.0)) for inch in range(1, 21)]

    # GA settings:
    MAX_ITERATION      = None
    PATIENCE_ITERATION = 50

    # Truss object:
    truss = Truss(3)
    truss.LoadFromJSON('./data/bar-120_input_0.json')

    # Do GA:
    ga = GA(truss, MEMBER_TYPE_LIST, ALLOWABLE_STRESS, ALLOWABLE_DISPLACEMENT, nIteration=MAX_ITERATION, nPatience=PATIENCE_ITERATION)
    minGene, (fitness, isInternalAllowed, isDisplaceAllowed), finalPop, bestFitnessHistory = ga.Evolve()

    # Translate optimal gene to member types:
    truss.SetMemberTypes(ga.TranslateGene(minGene))

    # Save result:
    truss.Solve()
    truss.DumpIntoJSON('bar-120_ga_0.json')


def TestGenerateCubeTruss():
    from sankethchebbi.generate import GenerateRandomCubeTrusses

    # Some parameters for your generated cube truss:
    GRID_RANGE                = (5, 5, 5)
    CUBE_NUMBER               = 7
    GENERATE_NUMBER           = 10
    EDGE_LENGTH_RANGE         = (100, 200)
    EXTERNAL_FORCE_RANGE      = [(-1000, 1000), (-1000, 1000), (-1000, 1000)]
    IS_DO_STRUCTURAL_ANALYSIS = True
    IS_PLOT_GENERATED_TRUSS   = True
    SAVE_FOLDER               = './generate'

    # Generate cube-like trusses:
    trussList = GenerateRandomCubeTrusses(gridRange=GRID_RANGE,
                                          numCubeRange=(CUBE_NUMBER, CUBE_NUMBER),
                                          numEachRange=(1, GENERATE_NUMBER),
                                          lengthRange=EDGE_LENGTH_RANGE,
                                          forceRange=EXTERNAL_FORCE_RANGE,
                                          isDoStructuralAnalysis=IS_DO_STRUCTURAL_ANALYSIS,
                                          isPlotTruss=IS_PLOT_GENERATED_TRUSS,
                                          saveFolder=SAVE_FOLDER,
                                          seed=42)
    return trussList


def TestDataAugmentation():
    from sankethchebbi.generate import GenerateRandomCubeTrusses
    from sankethchebbi.generate import MoveToCentroid, RandomTranslation, AddJointNoise, RandomResetPin, NoChange, TrussDataAugmenterList

    # Some parameters for your generated cube truss:
    GRID_RANGE                = (5, 5, 5)
    CUBE_NUMBER               = 4
    EDGE_LENGTH_RANGE         = (100, 200)
    EXTERNAL_FORCE_RANGE      = [(-1000, 1000), (-1000, 1000), (-1000, 1000)]
    IS_DO_STRUCTURAL_ANALYSIS = True
    IS_PLOT_GENERATED_TRUSS   = True
    SAVE_FOLDER               = './generate/augmentations'

    # Data augmentor:
    transforms = TrussDataAugmenterList(
        NoChange(),                                                         # Do nothing
        MoveToCentroid(),                                                   # Move the centroid of the truss to [0., 0., 0.]
        RandomTranslation(translateRange=[-30., 30.]),                      # Translate the whole truss randomly
        AddJointNoise(noiseMeans=[0., 0., 0.], noiseStds=[10., 10., 10.]),  # Add guassian noise to all positions of the joints
        RandomResetPin(minNumPin=5, maxNumPinRatio=0.6)                     # Reset the positions and number of pin supports
    )

    # Generate cube-like truss:
    truss = GenerateRandomCubeTrusses(gridRange=GRID_RANGE,
                                      numCubeRange=(CUBE_NUMBER, CUBE_NUMBER),
                                      numEachRange=(1, 1),
                                      lengthRange=EDGE_LENGTH_RANGE,
                                      forceRange=EXTERNAL_FORCE_RANGE,
                                      isDoStructuralAnalysis=IS_DO_STRUCTURAL_ANALYSIS,
                                      isPlotTruss=IS_PLOT_GENERATED_TRUSS,
                                      saveFolder=SAVE_FOLDER,
                                      seed=42,
                                      augmenter=transforms  # <- Do data augmentation !!!
                                    )[0]
    return truss


def TestTrussHeteroData():
    from sankethchebbi.data  import TrussHeteroDataCreator
    from sankethchebbi.type  import TaskType
    from sankethchebbi.truss import Truss

    JSON_FILE    = "./data/bar-25_input_0.json"
    TRUSS_DIM    = 3
    IS_USE_TRUSS = False

    # Creator to create PyG's HeteroData:
    creator = TrussHeteroDataCreator(taskType=TaskType.OPTIMIZATION)

    # Create PyG's HeteroData from JSON file or Truss object:
    if IS_USE_TRUSS:
        truss = Truss(TRUSS_DIM).LoadFromJSON(JSON_FILE)
        graph = creator.FromTruss(truss, trussSrc=JSON_FILE)
    else:
        graph = creator.FromJSON(JSON_FILE, TRUSS_DIM)

    # Print the structure of the HeteroData:
    print("Hetero Graph Structure:\n" + "-" * 50)
    print(graph)


if __name__ == '__main__':
    pass
    # TestTimeConsuming()
    # TestExample()
    # TestLoadFromJSON()
    # TestPlot()
    # TestGA()
    # TestGenerateCubeTruss()
    # TestDataAugmentation()
    # TestTrussHeteroData()
