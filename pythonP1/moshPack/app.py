# from ecommerce import shipping # allows for simple .function
import ecommerce.shipping as ship

from pathlib import Path

path = Path("ecommerce")
if not path.exists():
	raise ValueError("Path to Ecommerce does not exist")
	SystemExit(0)



ship.calc_shipping()
