# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from motor_controller/comand_msg_1.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class comand_msg_1(genpy.Message):
  _md5sum = "87a39e2f066462579da8199e99e51a53"
  _type = "motor_controller/comand_msg_1"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 mode
uint32 motor
int32 position

"""
  __slots__ = ['mode','motor','position']
  _slot_types = ['int32','uint32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       mode,motor,position

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(comand_msg_1, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.mode is None:
        self.mode = 0
      if self.motor is None:
        self.motor = 0
      if self.position is None:
        self.position = 0
    else:
      self.mode = 0
      self.motor = 0
      self.position = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_iIi.pack(_x.mode, _x.motor, _x.position))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.mode, _x.motor, _x.position,) = _struct_iIi.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_iIi.pack(_x.mode, _x.motor, _x.position))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.mode, _x.motor, _x.position,) = _struct_iIi.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_iIi = struct.Struct("<iIi")