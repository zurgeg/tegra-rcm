class RCMSig:
  def __init__(self, cmac_hash: list[int], rsa_pss_sig: list[int]):
    self.cmac_hash: int = cmac_hash
    self.rsa_pss_sig: int = rsa_pss_sig
class TegraRCMMessage:
  def __init__(self, len_insecure: int, 
               modulus: list[int], 
               sig: RCMSig, 
               reserved: list[int], 
               ecid: list[int], 
               opcode: int, 
               len_secure: int, 
               rcm_version: int, 
               args: list[int], 
               padding: list[int]):
               self.len_insecure: int = len_insecure
               self.modulus: list[int] = modulus
               self.sig: RCMSig = sig
               self.reserved: list[int] = reserved
               self.ecid: list[int] = ecid
               self.opcode: int = opcode
               self.len_secure: int = len_secure
               self.rcm_version: int = rcm_version
               self.args: list[int] = args
               self.padding: list[int] = padding
    
    
    
