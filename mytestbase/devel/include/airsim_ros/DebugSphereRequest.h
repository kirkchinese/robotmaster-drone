// Generated by gencpp from file airsim_ros/DebugSphereRequest.msg
// DO NOT EDIT!


#ifndef AIRSIM_ROS_MESSAGE_DEBUGSPHEREREQUEST_H
#define AIRSIM_ROS_MESSAGE_DEBUGSPHEREREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace airsim_ros
{
template <class ContainerAllocator>
struct DebugSphereRequest_
{
  typedef DebugSphereRequest_<ContainerAllocator> Type;

  DebugSphereRequest_()
    {
    }
  DebugSphereRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::airsim_ros::DebugSphereRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::airsim_ros::DebugSphereRequest_<ContainerAllocator> const> ConstPtr;

}; // struct DebugSphereRequest_

typedef ::airsim_ros::DebugSphereRequest_<std::allocator<void> > DebugSphereRequest;

typedef boost::shared_ptr< ::airsim_ros::DebugSphereRequest > DebugSphereRequestPtr;
typedef boost::shared_ptr< ::airsim_ros::DebugSphereRequest const> DebugSphereRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::airsim_ros::DebugSphereRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::airsim_ros::DebugSphereRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace airsim_ros

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::airsim_ros::DebugSphereRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::airsim_ros::DebugSphereRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::airsim_ros::DebugSphereRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::airsim_ros::DebugSphereRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::airsim_ros::DebugSphereRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::airsim_ros::DebugSphereRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::airsim_ros::DebugSphereRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::airsim_ros::DebugSphereRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::airsim_ros::DebugSphereRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "airsim_ros/DebugSphereRequest";
  }

  static const char* value(const ::airsim_ros::DebugSphereRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::airsim_ros::DebugSphereRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
;
  }

  static const char* value(const ::airsim_ros::DebugSphereRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::airsim_ros::DebugSphereRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct DebugSphereRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::airsim_ros::DebugSphereRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::airsim_ros::DebugSphereRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // AIRSIM_ROS_MESSAGE_DEBUGSPHEREREQUEST_H
