import trusspy as tp

M1 = tp.Model(logfile=False)

with M1.Nodes as MN:
    MN.add_node(1, coord=(0, 0, 0))
    MN.add_node(2, coord=(1, 0, 3))
    MN.add_node(3, coord=(2, 0, 0))

with M1.Elements as ME:
    ME.add_element(1, conn=(1, 2), gprop=[1])
    ME.add_element(2, conn=(2, 3), gprop=[1])

    E = 1  # elastic modulus
    ME.assign_material("all", [E])

with M1.Boundaries as MB:
    MB.add_bound_U(1, (0, 0, 0))
    MB.add_bound_U(2, (0, 0, 1))
    MB.add_bound_U(3, (0, 0, 0))

with M1.ExtForces as MF:
    MF.add_force(2, (0, 0, -1))

M1.Settings.incs = 150
M1.Settings.du = 0.01
M1.Settings.dlpf = 0.01
M1.Settings.xlimit = (1, 10)
M1.Settings.dlpf
M1.Settings.stepcontrol = True
M1.Settings.maxfac = 10

M1.build()
fig, ax = M1.plot_model(inc=0)

M1.run()
fig, ax = M1.plot_model(view="xz", contour="force", force_scale=2, inc=20)
fig1, ax1 = M1.plot_history(nodes=[2, 2], X="Displacement X", Y="Displacement Z")
fig2, ax2 = M1.plot_history(nodes=[2, 2], X="Displacement Z", Y="LPF")


