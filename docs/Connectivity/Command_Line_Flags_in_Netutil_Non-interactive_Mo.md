---
title: "Command Line Flags in Netutil Non-interactive Mode"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Command_Line_Flags_in_Netutil_Non-interactive_Mo.htm"
canonical_id: "actian-data-platform-command-line-flags-in-netutil-non-interactive-mo"
---

## Command Line Flags in Netutil Non-interactive Mode

The following command line flags are supported in netutil’s non-interactive mode:

**-u user**

:   Impersonate the specified user for the purpose of managing private authorization and connection entries. Only a user with the NET_ADMIN privilege (generally a system administrator) can impersonate another user.

**-file filename**

:   When this flag is used, netutil processes commands specified in the indicated input control file.

:   The format of the input control file is described in the following section.

**-file-**

:   If the input file is specified as "-" (a single hyphen character), input is taken from the standard input channel. This allows the user to enter commands directly from the keyboard or to run netutil as part of a Linux pipeline. To exit, press Ctrl+Z.

**-vnode vnode**

:   Connect to the Name server on the remote instance specified by the vnode name.

:   The vnode name must be defined on the local host's Name server; that is, connection and authorization information must exist locally for that vnode name. This information can be defined by invoking netutil on the local Name server.

### Input Control File

The input control file is an ASCII file that stores instructions about operations to be performed on the Name Server database. Each line of the file represents either a create, destroy, or show operation. These lines are called “input lines” in the remainder of this section.

The following conventions are observed:

- Blank lines are ignored in the control file.
- Case is insignificant except where significance is imposed by the usage of the data. For example, the login name on a Linux system has significant case.

- The character “#” indicates a comment; all text following a “#” character on any line is ignored.
- Input lines are divided into fields, which are separated by a blank space. For example, the following input line contains four fields:

```
show private login paulj
```

### Invariant Fields

The first four fields of an input line describe the action to be performed and the vnode with which the action is associated. These four fields appear in the order given below in every input line (except stop and quiesce server commands).

The following table defines these fields and their potential values:

| Field | Parameter | Value | Description |
| --- | --- | --- | --- |
| 1 | Function | Create, Destroy, or Show | The task that is performed. |
| 2 | Type | Global or Private | The registration type of the object.A global object is available to all users on the local node. A private object is available to a single user. |
| 3 | Object | Login or ConnectionAttribute | The object to be created, destroyed, or shown.“Connection” refers to a connection data entry.“Login” refers to a remote user authorization.“Attribute” refers to a vnode attribute entry. |
| 4 | Virtual Node Name | Vnode name | The virtual node name.Each line in the input control file must contain a vnode identifier. |

!!! note "Note"

    Values in any of the first three fields (Function, Type, and Object) can be abbreviated to a unique left substring. In practice, this means that a single-letter abbreviation is sufficient for any of these fields.

Values in the Virtual Node Name field cannot be abbreviated.

In addition to the four fields discussed above, other fields are required depending on the task to be accomplished by the input line. For example, an input line creating a remote user authorization requires an additional two fields: a login field and a password field. An input line creating or destroying a connection data entry requires an additional three fields: a network address field, a protocol field, and a listen address field.

For detailed information about additional fields, see the examples that follow.

### Wildcards

On input lines that specify either the Destroy or Show function, the asterisk character (*) can be entered as a wildcard in any field other than the Function, Type, and Object fields.

The asterisk character (*) indicates that the field is not to be used in selecting the data records to which the function is applied. Therefore, it is possible to destroy or display a number of records with a single input line.

!!! note "Note"

    Wildcards cannot be used with the Create function.
