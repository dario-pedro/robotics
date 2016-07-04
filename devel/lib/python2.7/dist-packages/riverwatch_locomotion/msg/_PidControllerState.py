# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from riverwatch_locomotion/PidControllerState.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class PidControllerState(genpy.Message):
  _md5sum = "0adb4d4aa5b0e13fb1d12b5f48903d9f"
  _type = "riverwatch_locomotion/PidControllerState"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
string name
bool PIDE
float64 set_point
float64 process_value
float64 error
float64 time_step
float64 command
float64 p
float64 i
float64 d
float64 integrator
float64 dervative
float64 proportional

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  __slots__ = ['header','name','PIDE','set_point','process_value','error','time_step','command','p','i','d','integrator','dervative','proportional']
  _slot_types = ['std_msgs/Header','string','bool','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,name,PIDE,set_point,process_value,error,time_step,command,p,i,d,integrator,dervative,proportional

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PidControllerState, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.name is None:
        self.name = ''
      if self.PIDE is None:
        self.PIDE = False
      if self.set_point is None:
        self.set_point = 0.
      if self.process_value is None:
        self.process_value = 0.
      if self.error is None:
        self.error = 0.
      if self.time_step is None:
        self.time_step = 0.
      if self.command is None:
        self.command = 0.
      if self.p is None:
        self.p = 0.
      if self.i is None:
        self.i = 0.
      if self.d is None:
        self.d = 0.
      if self.integrator is None:
        self.integrator = 0.
      if self.dervative is None:
        self.dervative = 0.
      if self.proportional is None:
        self.proportional = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.name = ''
      self.PIDE = False
      self.set_point = 0.
      self.process_value = 0.
      self.error = 0.
      self.time_step = 0.
      self.command = 0.
      self.p = 0.
      self.i = 0.
      self.d = 0.
      self.integrator = 0.
      self.dervative = 0.
      self.proportional = 0.

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
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_B11d.pack(_x.PIDE, _x.set_point, _x.process_value, _x.error, _x.time_step, _x.command, _x.p, _x.i, _x.d, _x.integrator, _x.dervative, _x.proportional))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8')
      else:
        self.name = str[start:end]
      _x = self
      start = end
      end += 89
      (_x.PIDE, _x.set_point, _x.process_value, _x.error, _x.time_step, _x.command, _x.p, _x.i, _x.d, _x.integrator, _x.dervative, _x.proportional,) = _struct_B11d.unpack(str[start:end])
      self.PIDE = bool(self.PIDE)
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
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_B11d.pack(_x.PIDE, _x.set_point, _x.process_value, _x.error, _x.time_step, _x.command, _x.p, _x.i, _x.d, _x.integrator, _x.dervative, _x.proportional))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8')
      else:
        self.name = str[start:end]
      _x = self
      start = end
      end += 89
      (_x.PIDE, _x.set_point, _x.process_value, _x.error, _x.time_step, _x.command, _x.p, _x.i, _x.d, _x.integrator, _x.dervative, _x.proportional,) = _struct_B11d.unpack(str[start:end])
      self.PIDE = bool(self.PIDE)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_B11d = struct.Struct("<B11d")
