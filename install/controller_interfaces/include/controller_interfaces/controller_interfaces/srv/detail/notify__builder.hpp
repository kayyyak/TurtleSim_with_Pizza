// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from controller_interfaces:srv/Notify.idl
// generated code does not contain a copyright notice

#ifndef CONTROLLER_INTERFACES__SRV__DETAIL__NOTIFY__BUILDER_HPP_
#define CONTROLLER_INTERFACES__SRV__DETAIL__NOTIFY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "controller_interfaces/srv/detail/notify__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace controller_interfaces
{

namespace srv
{

namespace builder
{

class Init_Notify_Request_status
{
public:
  Init_Notify_Request_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::controller_interfaces::srv::Notify_Request status(::controller_interfaces::srv::Notify_Request::_status_type arg)
  {
    msg_.status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::controller_interfaces::srv::Notify_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::controller_interfaces::srv::Notify_Request>()
{
  return controller_interfaces::srv::builder::Init_Notify_Request_status();
}

}  // namespace controller_interfaces


namespace controller_interfaces
{

namespace srv
{

namespace builder
{

class Init_Notify_Response_result
{
public:
  Init_Notify_Response_result()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::controller_interfaces::srv::Notify_Response result(::controller_interfaces::srv::Notify_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::controller_interfaces::srv::Notify_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::controller_interfaces::srv::Notify_Response>()
{
  return controller_interfaces::srv::builder::Init_Notify_Response_result();
}

}  // namespace controller_interfaces

#endif  // CONTROLLER_INTERFACES__SRV__DETAIL__NOTIFY__BUILDER_HPP_
