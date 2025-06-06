// Generated by gencpp from file airsim_ros/Circle.msg
// DO NOT EDIT!


#ifndef AIRSIM_ROS_MESSAGE_CIRCLE_H
#define AIRSIM_ROS_MESSAGE_CIRCLE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Vector3.h>

namespace airsim_ros
{
template <class ContainerAllocator>
struct Circle_
{
  typedef Circle_<ContainerAllocator> Type;

  // 构造函数
  Circle_()
    : index(0)
    , position()
    , yaw(0.0)  {
    }
  // 带分配器的构造函数
  Circle_(const ContainerAllocator& _alloc)
    : index(0)
    , position(_alloc)
    , yaw(0.0)  {
  (void)_alloc;
    }



   typedef uint8_t _index_type;
  _index_type index;

   typedef  ::geometry_msgs::Vector3_<ContainerAllocator>  _position_type;
  _position_type position;

   typedef double _yaw_type;
  _yaw_type yaw;





  typedef boost::shared_ptr< ::airsim_ros::Circle_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::airsim_ros::Circle_<ContainerAllocator> const> ConstPtr;

}; // struct Circle_

// 默认分配器的Circle类型
typedef ::airsim_ros::Circle_<std::allocator<void> > Circle;

// 默认分配器的Circle指针类型
typedef boost::shared_ptr< ::airsim_ros::Circle > CirclePtr;
typedef boost::shared_ptr< ::airsim_ros::Circle const> CircleConstPtr;

// 常量要求在行外定义



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::airsim_ros::Circle_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::airsim_ros::Circle_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::airsim_ros::Circle_<ContainerAllocator1> & lhs, const ::airsim_ros::Circle_<ContainerAllocator2> & rhs)
{
  return lhs.index == rhs.index &&
    lhs.position == rhs.position &&
    lhs.yaw == rhs.yaw;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::airsim_ros::Circle_<ContainerAllocator1> & lhs, const ::airsim_ros::Circle_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace airsim_ros

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::airsim_ros::Circle_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::airsim_ros::Circle_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::airsim_ros::Circle_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::airsim_ros::Circle_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::airsim_ros::Circle_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::airsim_ros::Circle_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::airsim_ros::Circle_<ContainerAllocator> >
{
  static const char* value()
  {
    return "182de38a68dfb7440273ce21ac6bad6d";
  }

  static const char* value(const ::airsim_ros::Circle_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x182de38a68dfb744ULL;
  static const uint64_t static_value2 = 0x0273ce21ac6bad6dULL;
};

template<class ContainerAllocator>
struct DataType< ::airsim_ros::Circle_<ContainerAllocator> >
{
  static const char* value()
  {
    return "airsim_ros/Circle";
  }

  static const char* value(const ::airsim_ros::Circle_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::airsim_ros::Circle_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 index\n"
"geometry_msgs/Vector3 position\n"
"float64 yaw\n"
"================================================================================\n"
"MSG: geometry_msgs/Vector3\n"
"# This represents a vector in free space. \n"
"# It is only meant to represent a direction. Therefore, it does not\n"
"# make sense to apply a translation to it (e.g., when applying a \n"
"# generic rigid transformation to a Vector3, tf2 will only apply the\n"
"# rotation). If you want your data to be translatable too, use the\n"
"# geometry_msgs/Point message instead.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
;
  }

  static const char* value(const ::airsim_ros::Circle_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::airsim_ros::Circle_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.index);
      stream.next(m.position);
      stream.next(m.yaw);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Circle_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::airsim_ros::Circle_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::airsim_ros::Circle_<ContainerAllocator>& v)
  {
    s << indent << "index: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.index);
    s << indent << "position: ";
    s << std::endl;
    Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "  ", v.position);
    s << indent << "yaw: ";
    Printer<double>::stream(s, indent + "  ", v.yaw);
  }
};

} // namespace message_operations
} // namespace ros

#endif // AIRSIM_ROS_MESSAGE_CIRCLE_H
