// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from controller_interfaces:srv/Notify.idl
// generated code does not contain a copyright notice

#ifndef CONTROLLER_INTERFACES__SRV__DETAIL__NOTIFY__STRUCT_H_
#define CONTROLLER_INTERFACES__SRV__DETAIL__NOTIFY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Notify in the package controller_interfaces.
typedef struct controller_interfaces__srv__Notify_Request
{
  bool status;
} controller_interfaces__srv__Notify_Request;

// Struct for a sequence of controller_interfaces__srv__Notify_Request.
typedef struct controller_interfaces__srv__Notify_Request__Sequence
{
  controller_interfaces__srv__Notify_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} controller_interfaces__srv__Notify_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Notify in the package controller_interfaces.
typedef struct controller_interfaces__srv__Notify_Response
{
  bool result;
} controller_interfaces__srv__Notify_Response;

// Struct for a sequence of controller_interfaces__srv__Notify_Response.
typedef struct controller_interfaces__srv__Notify_Response__Sequence
{
  controller_interfaces__srv__Notify_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} controller_interfaces__srv__Notify_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CONTROLLER_INTERFACES__SRV__DETAIL__NOTIFY__STRUCT_H_
