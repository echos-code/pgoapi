# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/catch_pokemon_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/catch_pokemon_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nCpogoprotos/networking/requests/messages/catch_pokemon_message.proto\x12\'pogoprotos.networking.requests.messages\x1a\'pogoprotos/inventory/item/item_id.proto\"\xe6\x01\n\x13\x43\x61tchPokemonMessage\x12\x14\n\x0c\x65ncounter_id\x18\x01 \x01(\x06\x12\x33\n\x08pokeball\x18\x02 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemId\x12\x1f\n\x17normalized_reticle_size\x18\x03 \x01(\x01\x12\x16\n\x0espawn_point_id\x18\x04 \x01(\t\x12\x13\n\x0bhit_pokemon\x18\x05 \x01(\x08\x12\x15\n\rspin_modifier\x18\x06 \x01(\x01\x12\x1f\n\x17normalized_hit_position\x18\x07 \x01(\x01\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CATCHPOKEMONMESSAGE = _descriptor.Descriptor(
  name='CatchPokemonMessage',
  full_name='pogoprotos.networking.requests.messages.CatchPokemonMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='encounter_id', full_name='pogoprotos.networking.requests.messages.CatchPokemonMessage.encounter_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokeball', full_name='pogoprotos.networking.requests.messages.CatchPokemonMessage.pokeball', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normalized_reticle_size', full_name='pogoprotos.networking.requests.messages.CatchPokemonMessage.normalized_reticle_size', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spawn_point_id', full_name='pogoprotos.networking.requests.messages.CatchPokemonMessage.spawn_point_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hit_pokemon', full_name='pogoprotos.networking.requests.messages.CatchPokemonMessage.hit_pokemon', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spin_modifier', full_name='pogoprotos.networking.requests.messages.CatchPokemonMessage.spin_modifier', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normalized_hit_position', full_name='pogoprotos.networking.requests.messages.CatchPokemonMessage.normalized_hit_position', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=384,
)

_CATCHPOKEMONMESSAGE.fields_by_name['pokeball'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
DESCRIPTOR.message_types_by_name['CatchPokemonMessage'] = _CATCHPOKEMONMESSAGE

CatchPokemonMessage = _reflection.GeneratedProtocolMessageType('CatchPokemonMessage', (_message.Message,), dict(
  DESCRIPTOR = _CATCHPOKEMONMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.catch_pokemon_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.CatchPokemonMessage)
  ))
_sym_db.RegisterMessage(CatchPokemonMessage)


# @@protoc_insertion_point(module_scope)
