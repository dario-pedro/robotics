// Generated by gencpp from file tr5_kinematics/DoInverseKinematic.msg
// DO NOT EDIT!


#ifndef TR5_KINEMATICS_MESSAGE_DOINVERSEKINEMATIC_H
#define TR5_KINEMATICS_MESSAGE_DOINVERSEKINEMATIC_H

#include <ros/service_traits.h>


#include <tr5_kinematics/DoInverseKinematicRequest.h>
#include <tr5_kinematics/DoInverseKinematicResponse.h>


namespace tr5_kinematics
{

struct DoInverseKinematic
{

typedef DoInverseKinematicRequest Request;
typedef DoInverseKinematicResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct DoInverseKinematic
} // namespace tr5_kinematics


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::tr5_kinematics::DoInverseKinematic > {
  static const char* value()
  {
    return "8124fdf484553a52e7b685afd1f774e4";
  }

  static const char* value(const ::tr5_kinematics::DoInverseKinematic&) { return value(); }
};

template<>
struct DataType< ::tr5_kinematics::DoInverseKinematic > {
  static const char* value()
  {
    return "tr5_kinematics/DoInverseKinematic";
  }

  static const char* value(const ::tr5_kinematics::DoInverseKinematic&) { return value(); }
};


// service_traits::MD5Sum< ::tr5_kinematics::DoInverseKinematicRequest> should match 
// service_traits::MD5Sum< ::tr5_kinematics::DoInverseKinematic > 
template<>
struct MD5Sum< ::tr5_kinematics::DoInverseKinematicRequest>
{
  static const char* value()
  {
    return MD5Sum< ::tr5_kinematics::DoInverseKinematic >::value();
  }
  static const char* value(const ::tr5_kinematics::DoInverseKinematicRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::tr5_kinematics::DoInverseKinematicRequest> should match 
// service_traits::DataType< ::tr5_kinematics::DoInverseKinematic > 
template<>
struct DataType< ::tr5_kinematics::DoInverseKinematicRequest>
{
  static const char* value()
  {
    return DataType< ::tr5_kinematics::DoInverseKinematic >::value();
  }
  static const char* value(const ::tr5_kinematics::DoInverseKinematicRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::tr5_kinematics::DoInverseKinematicResponse> should match 
// service_traits::MD5Sum< ::tr5_kinematics::DoInverseKinematic > 
template<>
struct MD5Sum< ::tr5_kinematics::DoInverseKinematicResponse>
{
  static const char* value()
  {
    return MD5Sum< ::tr5_kinematics::DoInverseKinematic >::value();
  }
  static const char* value(const ::tr5_kinematics::DoInverseKinematicResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::tr5_kinematics::DoInverseKinematicResponse> should match 
// service_traits::DataType< ::tr5_kinematics::DoInverseKinematic > 
template<>
struct DataType< ::tr5_kinematics::DoInverseKinematicResponse>
{
  static const char* value()
  {
    return DataType< ::tr5_kinematics::DoInverseKinematic >::value();
  }
  static const char* value(const ::tr5_kinematics::DoInverseKinematicResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // TR5_KINEMATICS_MESSAGE_DOINVERSEKINEMATIC_H
