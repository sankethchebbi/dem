from slientruss3d.truss import Truss
from slientruss3d.type  import SupportType, MemberType


def TestExample():
    # -------------------- Global variables --------------------
    TEST_OUTPUT_FILE    = f"./test_output.json"
    TRUSS_DIMENSION     = 3
    # ----------------------------------------------------------

    # Truss object:
    truss = Truss(dim=TRUSS_DIMENSION)

    # Truss settings:
    joints     = [(0, 0, 0), (360, 0, 0), (360, 180, 0), (0, 200, 0), (120, 100, 180)]
    supports   = [SupportType.PIN, SupportType.ROLLER_Z, SupportType.PIN, SupportType.PIN, SupportType.NO]
    forces     = [(1, (0, -10000, 5000))]
    members    = [(0, 4), (1, 4), (2, 4), (3, 4), (1, 2), (1, 3)]
    memberType = MemberType(1, 1e7, 1)

    # Read data in this [.py]:
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
    
    # Get result of structural analysis:
    displace, stress, resistance = truss.GetDisplacements(), truss.GetInternalStresses(), truss.GetResistances()
    return displace, stress, resistance
