// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from controller_interfaces:srv/Notify.idl
// generated code does not contain a copyright notice

#ifndef CONTROLLER_INTERFACES__SRV__DETAIL__NOTIFY__STRUCT_HPP_
#define CONTROLLER_INTERFACES__SRV__DETAIL__NOTIFY__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__controller_interfaces__srv__Notify_Request __attribute__((deprecated))
#else
# define DEPRECATED__controller_interfaces__srv__Notify_Request __declspec(deprecated)
#endif

namespace controller_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Notify_Request_
{
  using Type = Notify_Request_<ContainerAllocator>;

  explicit Notify_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = false;
    }
  }

  explicit Notify_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = false;
    }
  }

  // field types and members
  using _status_type =
    bool;
  _status_type status;

  // setters for named parameter idiom
  Type & set__status(
    const bool & _arg)
  {
    this->status = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    controller_interfaces::srv::Notify_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const controller_interfaces::srv::Notify_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<controller_interfaces::srv::Notify_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<controller_interfaces::srv::Notify_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      controller_interfaces::srv::Notify_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<controller_interfaces::srv::Notify_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      controller_interfaces::srv::Notify_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<controller_interfaces::srv::Notify_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<controller_interfaces::srv::Notify_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<controller_interfaces::srv::Notify_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__controller_interfaces__srv__Notify_Request
    std::shared_ptr<controller_interfaces::srv::Notify_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__controller_interfaces__srv__Notify_Request
    std::shared_ptr<controller_interfaces::srv::Notify_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Notify_Request_ & other) const
  {
    if (this->status != other.status) {
      return false;
    }
    return true;
  }
  bool operator!=(const Notify_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Notify_Request_

// alias to use template instance with default allocator
using Notify_Request =
  controller_interfaces::srv::Notify_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace controller_interfaces


#ifndef _WIN32
# define DEPRECATED__controller_interfaces__srv__Notify_Response __attribute__((deprecated))
#else
# define DEPRECATED__controller_interfaces__srv__Notify_Response __declspec(deprecated)
#endif

namespace controller_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Notify_Response_
{
  using Type = Notify_Response_<ContainerAllocator>;

  explicit Notify_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->result = false;
    }
  }

  explicit Notify_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->result = false;
    }
  }

  // field types and members
  using _result_type =
    bool;
  _result_type result;

  // setters for named parameter idiom
  Type & set__result(
    const bool & _arg)
  {
    this->result = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    controller_interfaces::srv::Notify_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const controller_interfaces::srv::Notify_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<controller_interfaces::srv::Notify_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<controller_interfaces::srv::Notify_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      controller_interfaces::srv::Notify_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<controller_interfaces::srv::Notify_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      controller_interfaces::srv::Notify_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<controller_interfaces::srv::Notify_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<controller_interfaces::srv::Notify_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<controller_interfaces::srv::Notify_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__controller_interfaces__srv__Notify_Response
    std::shared_ptr<controller_interfaces::srv::Notify_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__controller_interfaces__srv__Notify_Response
    std::shared_ptr<controller_interfaces::srv::Notify_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Notify_Response_ & other) const
  {
    if (this->result != other.result) {
      return false;
    }
    return true;
  }
  bool operator!=(const Notify_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Notify_Response_

// alias to use template instance with default allocator
using Notify_Response =
  controller_interfaces::srv::Notify_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace controller_interfaces

namespace controller_interfaces
{

namespace srv
{

struct Notify
{
  using Request = controller_interfaces::srv::Notify_Request;
  using Response = controller_interfaces::srv::Notify_Response;
};

}  // namespace srv

}  // namespace controller_interfaces

#endif  // CONTROLLER_INTERFACES__SRV__DETAIL__NOTIFY__STRUCT_HPP_
