"""
routing.py: defines services provided by the collection of protocols
"""
from typing import Tuple

import netaddr

from core.emane.nodes import EmaneNet
from core.emulator.enumerations import LinkTypes
from core.nodes.base import CoreNode
from core.nodes.interface import DEFAULT_MTU, CoreInterface
from core.nodes.network import PtpNet, WlanNode
from core.nodes.physical import Rj45Node
from core.services.coreservices import CoreService


def addrstr(ip: netaddr.IPNetwork) -> str:
  """
  helper for mapping IP addresses to config statements
  """
  address = str(ip.ip)
  if netaddr.valid_ipv4(address):
      return "ip address %s" % ip
  elif netaddr.valid_ipv6(address):
      return "ipv6 address %s" % ip
  else:
      raise ValueError("invalid address: %s", ip)

class Hello(CoreService):
  name: str = "Hello"
  group: str = "Networking"

  # configs: Tuple[str, ...] = ("hello.conf", "helloboot.sh", "log")
  configs: Tuple[str, ...] = ("hello.conf", "helloboot.sh")

  startup: Tuple[str, ...] = ("bash helloboot.sh", )

  # shutdown: Tuple[str, ...] = ("killall server", "killall client")

  @classmethod
  def generate_config(cls, node: CoreNode, filename: str) -> None:
    if filename == cls.configs[0]:
      return cls.generate_hello_conf(node)
    elif filename == cls.configs[1]:
      return cls.generate_hello_boot(node)
    # elif filename == cls.configs[2]:
    #   return ""
    else:
      raise ValueError("file name (%s) is not a known configuration: %s",
                       filename, cls.configs)

  @classmethod
  def generate_hello_conf(cls, node: CoreNode) -> str:
    cfg = ""
    for iface in node.get_ifaces():
      cfg += "interface %s\n" % iface.name
      cfg += "\n".join(map(addrstr, iface.ip4s))
      cfg += "\n!\n"
    return cfg

  @classmethod
  def generate_hello_boot(cls, node: CoreNode) -> str:
    """
    Generate shell script used to boot the daemons
    """
    return """\
#!/bin/sh
# auto-generated by hello service (networking.py)

touch server.log
chmod 777 server.log
/home/ben/projects/routing/hello/build/server -d

# touch client.log
# chmod 777 client.log
# /home/ben/projects/routing/hello/build/client -d

"""
