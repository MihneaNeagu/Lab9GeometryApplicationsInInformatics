from geomdl import BSpline
from geomdl import multi
# Import Matplotlib visualization module
from geomdl.visualization import VisMPL
# Create the curve instance
crv1 = BSpline.Curve()
crv2 = BSpline.Curve()
# Set degree
crv1.degree = 2
crv2.degree = 3
# Set control points
crv1.ctrlpts = [[-2, -3], [-1, 2], [2, 2], [3, 0], [1, -3]]
crv2.ctrlpts = [[1.87, 9.37], [5.62, 0], [2, -4], [-3.15, -4.73]]
# Set knot vector
crv1.knotvector = [0.5, 0.8, 1.4, 2.1, 2.4, 2.9, 4.0, 4.5, 4.9]
crv2.knotvector = [0.5, 0.8, 1.4, 2.1, 2.4, 2.9, 4.0]
c = multi.CurveContainer([crv1, crv2])
# Set the visualization component of the curve
c.vis = VisMPL.VisCurve2D()


# Plot the curve
c.render()