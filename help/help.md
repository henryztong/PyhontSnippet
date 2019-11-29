The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
Help on package mysql.connector in mysql:

NAME
    mysql.connector - MySQL Connector/Python - MySQL driver written in Python

PACKAGE CONTENTS
    abstracts
    authentication
    catch23
    charsets
    connection
    connection_cext
    constants
    conversion
    cursor
    cursor_cext
    custom_types
    dbapi
    django (package)
    errorcode
    errors
    locales (package)
    network
    optionfiles
    pooling
    protocol
    utils
    version

CLASSES
    builtins.Exception(builtins.BaseException)
        mysql.connector.errors.Error
            mysql.connector.errors.DatabaseError
                mysql.connector.errors.DataError
                mysql.connector.errors.IntegrityError
                mysql.connector.errors.InternalError
                mysql.connector.errors.NotSupportedError
                mysql.connector.errors.OperationalError
                mysql.connector.errors.ProgrammingError
            mysql.connector.errors.InterfaceError
        mysql.connector.errors.Warning
    builtins.object
        builtins.bytes
        datetime.date
            datetime.datetime
        datetime.time
    mysql.connector.abstracts.MySQLConnectionAbstract(mysql.connector.abstracts.MySQLConnectionAbstract, builtins.object)
        mysql.connector.connection.MySQLConnection
        mysql.connector.connection_cext.CMySQLConnection
    mysql.connector.constants._Constants(builtins.object)
        mysql.connector.constants.CharacterSet
        mysql.connector.constants.FieldType
        mysql.connector.constants.RefreshOption
    mysql.connector.constants._Flags(mysql.connector.constants._Constants)
        mysql.connector.constants.ClientFlag
        mysql.connector.constants.FieldFlag
    
    Binary = class bytes(object)
     |  bytes(iterable_of_ints) -> bytes
     |  bytes(string, encoding[, errors]) -> bytes
     |  bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
     |  bytes(int) -> bytes object of size given by the parameter initialized with null bytes
     |  bytes() -> empty bytes object
     |  
     |  Construct an immutable array of bytes from:
     |    - an iterable yielding integers in range(256)
     |    - a text string encoded using the specified encoding
     |    - any object implementing the buffer API.
     |    - an integer
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.n
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return self*value.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  capitalize(...)
     |      B.capitalize() -> copy of B
     |      
     |      Return a copy of B with only its first character capitalized (ASCII)
     |      and the rest lower-cased.
     |  
     |  center(...)
     |      B.center(width[, fillchar]) -> copy of B
     |      
     |      Return B centered in a string of length width.  Padding is
     |      done using the specified fill character (default is a space).
     |  
     |  count(...)
     |      B.count(sub[, start[, end]]) -> int
     |      
     |      Return the number of non-overlapping occurrences of subsection sub in
     |      bytes B[start:end].  Optional arguments start and end are interpreted
     |      as in slice notation.
     |  
     |  decode(self, /, encoding='utf-8', errors='strict')
     |      Decode the bytes using the codec registered for encoding.
     |      
     |      encoding
     |        The encoding with which to decode the bytes.
     |      errors
     |        The error handling scheme to use for the handling of decoding errors.
     |        The default is 'strict' meaning that decoding errors raise a
     |        UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
     |        as well as any other name registered with codecs.register_error that
     |        can handle UnicodeDecodeErrors.
     |  
     |  endswith(...)
     |      B.endswith(suffix[, start[, end]]) -> bool
     |      
     |      Return True if B ends with the specified suffix, False otherwise.
     |      With optional start, test B beginning at that position.
     |      With optional end, stop comparing B at that position.
     |      suffix can also be a tuple of bytes to try.
     |  
     |  expandtabs(...)
     |      B.expandtabs(tabsize=8) -> copy of B
     |      
     |      Return a copy of B where all tab characters are expanded using spaces.
     |      If tabsize is not given, a tab size of 8 characters is assumed.
     |  
     |  find(...)
     |      B.find(sub[, start[, end]]) -> int
     |      
     |      Return the lowest index in B where subsection sub is found,
     |      such that sub is contained within B[start,end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Return -1 on failure.
     |  
     |  fromhex(string, /) from builtins.type
     |      Create a bytes object from a string of hexadecimal numbers.
     |      
     |      Spaces between two numbers are accepted.
     |      Example: bytes.fromhex('B9 01EF') -> b'\\xb9\\x01\\xef'.
     |  
     |  hex(...)
     |      B.hex() -> string
     |      
     |      Create a string of hexadecimal numbers from a bytes object.
     |      Example: b'\xb9\x01\xef'.hex() -> 'b901ef'.
     |  
     |  index(...)
     |      B.index(sub[, start[, end]]) -> int
     |      
     |      Return the lowest index in B where subsection sub is found,
     |      such that sub is contained within B[start,end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Raises ValueError when the subsection is not found.
     |  
     |  isalnum(...)
     |      B.isalnum() -> bool
     |      
     |      Return True if all characters in B are alphanumeric
     |      and there is at least one character in B, False otherwise.
     |  
     |  isalpha(...)
     |      B.isalpha() -> bool
     |      
     |      Return True if all characters in B are alphabetic
     |      and there is at least one character in B, False otherwise.
     |  
     |  isdigit(...)
     |      B.isdigit() -> bool
     |      
     |      Return True if all characters in B are digits
     |      and there is at least one character in B, False otherwise.
     |  
     |  islower(...)
     |      B.islower() -> bool
     |      
     |      Return True if all cased characters in B are lowercase and there is
     |      at least one cased character in B, False otherwise.
     |  
     |  isspace(...)
     |      B.isspace() -> bool
     |      
     |      Return True if all characters in B are whitespace
     |      and there is at least one character in B, False otherwise.
     |  
     |  istitle(...)
     |      B.istitle() -> bool
     |      
     |      Return True if B is a titlecased string and there is at least one
     |      character in B, i.e. uppercase characters may only follow uncased
     |      characters and lowercase characters only cased ones. Return False
     |      otherwise.
     |  
     |  isupper(...)
     |      B.isupper() -> bool
     |      
     |      Return True if all cased characters in B are uppercase and there is
     |      at least one cased character in B, False otherwise.
     |  
     |  join(self, iterable_of_bytes, /)
     |      Concatenate any number of bytes objects.
     |      
     |      The bytes whose method is called is inserted in between each pair.
     |      
     |      The result is returned as a new bytes object.
     |      
     |      Example: b'.'.join([b'ab', b'pq', b'rs']) -> b'ab.pq.rs'.
     |  
     |  ljust(...)
     |      B.ljust(width[, fillchar]) -> copy of B
     |      
     |      Return B left justified in a string of length width. Padding is
     |      done using the specified fill character (default is a space).
     |  
     |  lower(...)
     |      B.lower() -> copy of B
     |      
     |      Return a copy of B with all ASCII characters converted to lowercase.
     |  
     |  lstrip(self, bytes=None, /)
     |      Strip leading bytes contained in the argument.
     |      
     |      If the argument is omitted or None, strip leading  ASCII whitespace.
     |  
     |  partition(self, sep, /)
     |      Partition the bytes into three parts using the given separator.
     |      
     |      This will search for the separator sep in the bytes. If the separator is found,
     |      returns a 3-tuple containing the part before the separator, the separator
     |      itself, and the part after it.
     |      
     |      If the separator is not found, returns a 3-tuple containing the original bytes
     |      object and two empty bytes objects.
     |  
     |  replace(self, old, new, count=-1, /)
     |      Return a copy with all occurrences of substring old replaced by new.
     |      
     |        count
     |          Maximum number of occurrences to replace.
     |          -1 (the default value) means replace all occurrences.
     |      
     |      If the optional argument count is given, only the first count occurrences are
     |      replaced.
     |  
     |  rfind(...)
     |      B.rfind(sub[, start[, end]]) -> int
     |      
     |      Return the highest index in B where subsection sub is found,
     |      such that sub is contained within B[start,end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Return -1 on failure.
     |  
     |  rindex(...)
     |      B.rindex(sub[, start[, end]]) -> int
     |      
     |      Return the highest index in B where subsection sub is found,
     |      such that sub is contained within B[start,end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Raise ValueError when the subsection is not found.
     |  
     |  rjust(...)
     |      B.rjust(width[, fillchar]) -> copy of B
     |      
     |      Return B right justified in a string of length width. Padding is
     |      done using the specified fill character (default is a space)
     |  
     |  rpartition(self, sep, /)
     |      Partition the bytes into three parts using the given separator.
     |      
     |      This will search for the separator sep in the bytes, starting at the end. If
     |      the separator is found, returns a 3-tuple containing the part before the
     |      separator, the separator itself, and the part after it.
     |      
     |      If the separator is not found, returns a 3-tuple containing two empty bytes
     |      objects and the original bytes object.
     |  
     |  rsplit(self, /, sep=None, maxsplit=-1)
     |      Return a list of the sections in the bytes, using sep as the delimiter.
     |      
     |        sep
     |          The delimiter according which to split the bytes.
     |          None (the default value) means split on ASCII whitespace characters
     |          (space, tab, return, newline, formfeed, vertical tab).
     |        maxsplit
     |          Maximum number of splits to do.
     |          -1 (the default value) means no limit.
     |      
     |      Splitting is done starting at the end of the bytes and working to the front.
     |  
     |  rstrip(self, bytes=None, /)
     |      Strip trailing bytes contained in the argument.
     |      
     |      If the argument is omitted or None, strip trailing ASCII whitespace.
     |  
     |  split(self, /, sep=None, maxsplit=-1)
     |      Return a list of the sections in the bytes, using sep as the delimiter.
     |      
     |      sep
     |        The delimiter according which to split the bytes.
     |        None (the default value) means split on ASCII whitespace characters
     |        (space, tab, return, newline, formfeed, vertical tab).
     |      maxsplit
     |        Maximum number of splits to do.
     |        -1 (the default value) means no limit.
     |  
     |  splitlines(self, /, keepends=False)
     |      Return a list of the lines in the bytes, breaking at line boundaries.
     |      
     |      Line breaks are not included in the resulting list unless keepends is given and
     |      true.
     |  
     |  startswith(...)
     |      B.startswith(prefix[, start[, end]]) -> bool
     |      
     |      Return True if B starts with the specified prefix, False otherwise.
     |      With optional start, test B beginning at that position.
     |      With optional end, stop comparing B at that position.
     |      prefix can also be a tuple of bytes to try.
     |  
     |  strip(self, bytes=None, /)
     |      Strip leading and trailing bytes contained in the argument.
     |      
     |      If the argument is omitted or None, strip leading and trailing ASCII whitespace.
     |  
     |  swapcase(...)
     |      B.swapcase() -> copy of B
     |      
     |      Return a copy of B with uppercase ASCII characters converted
     |      to lowercase ASCII and vice versa.
     |  
     |  title(...)
     |      B.title() -> copy of B
     |      
     |      Return a titlecased version of B, i.e. ASCII words start with uppercase
     |      characters, all remaining cased characters have lowercase.
     |  
     |  translate(self, table, /, delete=b'')
     |      Return a copy with each character mapped by the given translation table.
     |      
     |        table
     |          Translation table, which must be a bytes object of length 256.
     |      
     |      All characters occurring in the optional argument delete are removed.
     |      The remaining characters are mapped through the given translation table.
     |  
     |  upper(...)
     |      B.upper() -> copy of B
     |      
     |      Return a copy of B with all ASCII characters converted to uppercase.
     |  
     |  zfill(...)
     |      B.zfill(width) -> copy of B
     |      
     |      Pad a numeric string B with zeros on the left, to fill a field
     |      of the specified width.  B is never truncated.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  maketrans(frm, to, /)
     |      Return a translation table useable for the bytes or bytearray translate method.
     |      
     |      The returned table will be one where each byte in frm is mapped to the byte at
     |      the same position in to.
     |      
     |      The bytes objects frm and to must be of the same length.
    
    class CMySQLConnection(mysql.connector.abstracts.MySQLConnectionAbstract)
     |  Class initiating a MySQL Connection using Connector/C
     |  
     |  Method resolution order:
     |      CMySQLConnection
     |      mysql.connector.abstracts.MySQLConnectionAbstract
     |      mysql.connector.abstracts.MySQLConnectionAbstract
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, **kwargs)
     |      Initialization
     |  
     |  close(self)
     |      Disconnect from the MySQL server
     |  
     |  cmd_change_user(self, username='', password='', database='', charset=45)
     |      Change the current logged in user
     |  
     |  cmd_init_db(self, database)
     |      Change the current database
     |  
     |  cmd_process_kill(self, mysql_pid)
     |      Kill a MySQL process
     |  
     |  cmd_query(self, query, raw=None, buffered=False, raw_as_string=False)
     |      Send a query to the MySQL server
     |  
     |  cmd_quit(self)
     |      Close the current connection with the server
     |  
     |  cmd_refresh(self, options)
     |      Send the Refresh command to the MySQL server
     |  
     |  cmd_shutdown(self, shutdown_type=None)
     |      Shut down the MySQL Server
     |  
     |  cmd_statistics(self)
     |      Return statistics from the MySQL server
     |  
     |  commit(self)
     |      Commit current transaction
     |  
     |  consume_results(self)
     |      Consume the current result
     |      
     |      This method consume the result by reading (consuming) all rows.
     |  
     |  cursor(self, buffered=None, raw=None, prepared=None, cursor_class=None, dictionary=None, named_tuple=None)
     |      Instantiates and returns a cursor using C Extension
     |      
     |      By default, CMySQLCursor is returned. Depending on the options
     |      while connecting, a buffered and/or raw cursor is instantiated
     |      instead. Also depending upon the cursor options, rows can be
     |      returned as dictionary or named tuple.
     |      
     |      Dictionary and namedtuple based cursors are available with buffered
     |      output but not raw.
     |      
     |      It is possible to also give a custom cursor through the
     |      cursor_class parameter, but it needs to be a subclass of
     |      mysql.connector.cursor_cext.CMySQLCursor.
     |      
     |      Raises ProgrammingError when cursor_class is not a subclass of
     |      CursorBase. Raises ValueError when cursor is not available.
     |      
     |      Returns instance of CMySQLCursor or subclass.
     |      
     |      :param buffered: Return a buffering cursor
     |      :param raw: Return a raw cursor
     |      :param prepared: Return a cursor which uses prepared statements
     |      :param cursor_class: Use a custom cursor class
     |      :param dictionary: Rows are returned as dictionary
     |      :param named_tuple: Rows are returned as named tuple
     |      :return: Subclass of CMySQLCursor
     |      :rtype: CMySQLCursor or subclass
     |  
     |  disconnect = close(self)
     |  
     |  fetch_eof_columns(self)
     |      Fetch EOF and column information
     |  
     |  fetch_eof_status(self)
     |      Fetch EOF and status information
     |  
     |  free_result(self)
     |      Frees the result
     |  
     |  get_row(self, binary=False, columns=None, raw=None)
     |      Get the next rows returned by the MySQL server
     |  
     |  get_rows(self, count=None, binary=False, columns=None, raw=None)
     |      Get all or a subset of rows returned by the MySQL server
     |  
     |  handle_unread_result(self)
     |      Check whether there is an unread result
     |  
     |  info_query(self, query)
     |      Send a query which only returns 1 row
     |  
     |  is_connected(self)
     |      Reports whether the connection to MySQL Server is available
     |  
     |  next_result(self)
     |      Reads the next result
     |  
     |  ping(self, reconnect=False, attempts=1, delay=0)
     |      Check availability of the MySQL server
     |      
     |      When reconnect is set to True, one or more attempts are made to try
     |      to reconnect to the MySQL server using the reconnect()-method.
     |      
     |      delay is the number of seconds to wait between each retry.
     |      
     |      When the connection is not available, an InterfaceError is raised. Use
     |      the is_connected()-method if you just want to check the connection
     |      without raising an error.
     |      
     |      Raises InterfaceError on errors.
     |  
     |  prepare_for_mysql(self, params)
     |      Prepare parameters for statements
     |      
     |      This method is use by cursors to prepared parameters found in the
     |      list (or tuple) params.
     |      
     |      Returns dict.
     |  
     |  rollback(self)
     |      Rollback current transaction
     |  
     |  set_character_set_name(self, charset)
     |      Sets the default character set name for current connection.
     |  
     |  set_unicode(self, value=True)
     |      Toggle unicode mode
     |      
     |      Set whether we return string fields as unicode or not.
     |      Default is True.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  autocommit
     |      Get whether autocommit is on or off
     |  
     |  connection_id
     |      MySQL connection ID
     |  
     |  database
     |      Get the current database
     |  
     |  in_transaction
     |      MySQL session has started a transaction
     |  
     |  more_results
     |      Check if there are more results
     |  
     |  num_rows
     |      Returns number of rows of current result set
     |  
     |  result_set_available
     |      Check if a result set is available
     |  
     |  unread_result
     |      Check if there are unread results or rows
     |  
     |  warning_count
     |      Returns number of warnings
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __abstractmethods__ = frozenset()
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from mysql.connector.abstracts.MySQLConnectionAbstract:
     |  
     |  cmd_debug(self)
     |      Send the DEBUG command
     |  
     |  cmd_ping(self)
     |      Send the PING command
     |  
     |  cmd_process_info(self)
     |      Get the process list of the MySQL Server
     |      
     |      This method is a placeholder to notify that the PROCESS_INFO command
     |      is not supported by raising the NotSupportedError. The command
     |      "SHOW PROCESSLIST" should be send using the cmd_query()-method or
     |      using the INFORMATION_SCHEMA database.
     |      
     |      Raises NotSupportedError exception
     |  
     |  cmd_query_iter(self, statements)
     |      Send one or more statements to the MySQL server
     |  
     |  cmd_reset_connection(self)
     |      Resets the session state without re-authenticating
     |  
     |  cmd_stmt_close(self, statement_id)
     |      Deallocate a prepared MySQL statement
     |  
     |  cmd_stmt_execute(self, statement_id, data=(), parameters=(), flags=0)
     |      Execute a prepared MySQL statement
     |  
     |  cmd_stmt_prepare(self, statement)
     |      Prepare a MySQL statement
     |  
     |  cmd_stmt_reset(self, statement_id)
     |      Reset data for prepared statement sent as long data
     |  
     |  cmd_stmt_send_long_data(self, statement_id, param_id, data)
     |      Send data for a column
     |  
     |  config(self, **kwargs)
     |      Configure the MySQL Connection
     |      
     |      This method allows you to configure the MySQLConnection instance.
     |      
     |      Raises on errors.
     |  
     |  connect(self, **kwargs)
     |      Connect to the MySQL server
     |      
     |      This method sets up the connection to the MySQL server. If no
     |      arguments are given, it will use the already configured or default
     |      values.
     |  
     |  get_server_info(self)
     |      Get the original MySQL version information
     |      
     |      This method returns the original MySQL server as text. If not
     |      previously connected, it will return None.
     |      
     |      Returns a string or None.
     |  
     |  get_server_version(self)
     |      Get the MySQL version
     |      
     |      This method returns the MySQL server version as a tuple. If not
     |      previously connected, it will return None.
     |      
     |      Returns a tuple or None.
     |  
     |  isset_client_flag(self, flag)
     |      Check if a client flag is set
     |  
     |  reconnect(self, attempts=1, delay=0)
     |      Attempt to reconnect to the MySQL server
     |      
     |      The argument attempts should be the number of times a reconnect
     |      is tried. The delay argument is the number of seconds to wait between
     |      each retry.
     |      
     |      You may want to set the number of attempts higher and use delay when
     |      you expect the MySQL server to be down for maintenance or when you
     |      expect the network to be temporary unavailable.
     |      
     |      Raises InterfaceError on errors.
     |  
     |  reset_session(self, user_variables=None, session_variables=None)
     |      Clears the current active session
     |      
     |      This method resets the session state, if the MySQL server is 5.7.3
     |      or later active session will be reset without re-authenticating.
     |      For other server versions session will be reset by re-authenticating.
     |      
     |      It is possible to provide a sequence of variables and their values to
     |      be set after clearing the session. This is possible for both user
     |      defined variables and session variables.
     |      This method takes two arguments user_variables and session_variables
     |      which are dictionaries.
     |      
     |      Raises OperationalError if not connected, InternalError if there are
     |      unread results and InterfaceError on errors.
     |  
     |  set_charset_collation(self, charset=None, collation=None)
     |      Sets the character set and collation for the current connection
     |      
     |      This method sets the character set and collation to be used for
     |      the current connection. The charset argument can be either the
     |      name of a character set as a string, or the numerical equivalent
     |      as defined in constants.CharacterSet.
     |      
     |      When the collation is not given, the default will be looked up and
     |      used.
     |      
     |      For example, the following will set the collation for the latin1
     |      character set to latin1_general_ci:
     |      
     |         set_charset('latin1','latin1_general_ci')
     |  
     |  set_client_flags(self, flags)
     |      Set the client flags
     |      
     |      The flags-argument can be either an int or a list (or tuple) of
     |      ClientFlag-values. If it is an integer, it will set client_flags
     |      to flags as is.
     |      If flags is a list (or tuple), each flag will be set or unset
     |      when it's negative.
     |      
     |      set_client_flags([ClientFlag.FOUND_ROWS,-ClientFlag.LONG_FLAG])
     |      
     |      Raises ProgrammingError when the flags argument is not a set or
     |      an integer bigger than 0.
     |      
     |      Returns self.client_flags
     |  
     |  set_converter_class(self, convclass)
     |      Set the converter class to be used. This should be a class overloading
     |      methods and members of conversion.MySQLConverter.
     |  
     |  set_login(self, username=None, password=None)
     |      Set login information for MySQL
     |      
     |      Set the username and/or password for the user connecting to
     |      the MySQL Server.
     |  
     |  start_transaction(self, consistent_snapshot=False, isolation_level=None, readonly=None)
     |      Start a transaction
     |      
     |      This method explicitly starts a transaction sending the
     |      START TRANSACTION statement to the MySQL server. You can optionally
     |      set whether there should be a consistent snapshot, which
     |      isolation level you need or which access mode i.e. READ ONLY or
     |      READ WRITE.
     |      
     |      For example, to start a transaction with isolation level SERIALIZABLE,
     |      you would do the following:
     |          >>> cnx = mysql.connector.connect(..)
     |          >>> cnx.start_transaction(isolation_level='SERIALIZABLE')
     |      
     |      Raises ProgrammingError when a transaction is already in progress
     |      and when ValueError when isolation_level specifies an Unknown
     |      level.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from mysql.connector.abstracts.MySQLConnectionAbstract:
     |  
     |  can_consume_results
     |      Returns whether to consume results
     |  
     |  charset
     |      Returns the character set for current connection
     |      
     |      This property returns the character set name of the current connection.
     |      The server is queried when the connection is active. If not connected,
     |      the configured character set name is returned.
     |      
     |      Returns a string.
     |  
     |  collation
     |      Returns the collation for current connection
     |      
     |      This property returns the collation name of the current connection.
     |      The server is queried when the connection is active. If not connected,
     |      the configured collation name is returned.
     |      
     |      Returns a string.
     |  
     |  get_warnings
     |      Get whether this connection retrieves warnings automatically
     |      
     |      This method returns whether this connection retrieves warnings
     |      automatically.
     |      
     |      Returns True, or False when warnings are not retrieved.
     |  
     |  python_charset
     |      Returns the Python character set for current connection
     |      
     |      This property returns the character set name of the current connection.
     |      Note that, unlike property charset, this checks if the previously set
     |      character set is supported by Python and if not, it returns the
     |      equivalent character set that Python supports.
     |      
     |      Returns a string.
     |  
     |  raise_on_warnings
     |      Get whether this connection raises an error on warnings
     |      
     |      This method returns whether this connection will raise errors when
     |      MySQL reports warnings.
     |      
     |      Returns True or False.
     |  
     |  server_host
     |      MySQL server IP address or name
     |  
     |  server_port
     |      MySQL server TCP/IP port
     |  
     |  sql_mode
     |      Get the SQL mode
     |  
     |  time_zone
     |      Get the current time zone
     |  
     |  unix_socket
     |      MySQL Unix socket file location
     |  
     |  user
     |      User used while connecting to MySQL
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from mysql.connector.abstracts.MySQLConnectionAbstract:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class CharacterSet(_Constants)
     |  MySQL supported character sets and collations
     |  
     |  List of character sets with their collations supported by MySQL. This
     |  maps to the character set we get from the server within the handshake
     |  packet.
     |  
     |  The list is hardcode so we avoid a database query when getting the
     |  name of the used character set or collation.
     |  
     |  Method resolution order:
     |      CharacterSet
     |      _Constants
     |      builtins.object
     |  
     |  Class methods defined here:
     |  
     |  get_charset_info(charset=None, collation=None) from builtins.type
     |      Get character set information using charset name and/or collation
     |      
     |      Retrieves character set and collation information given character
     |      set name and/or a collation name.
     |      If charset is an integer, it will look up the character set based
     |      on the MySQL's ID.
     |      For example:
     |          get_charset_info('utf8',None)
     |          get_charset_info(collation='utf8_general_ci')
     |          get_charset_info(47)
     |      
     |      Raises ProgrammingError when character set is not supported.
     |      
     |      Returns a tuple with (id, characterset name, collation)
     |  
     |  get_default_collation(charset) from builtins.type
     |      Retrieves the default collation for given character set
     |      
     |      Raises ProgrammingError when character set is not supported.
     |      
     |      Returns list (collation, charset, index)
     |  
     |  get_desc(name) from builtins.type
     |      Retrieves character set information as string using an ID
     |      
     |      Retrieves character set and collation information based on the
     |      given MySQL ID.
     |      
     |      Returns a tuple.
     |  
     |  get_info(setid) from builtins.type
     |      Retrieves character set information as tuple using an ID
     |      
     |      Retrieves character set and collation information based on the
     |      given MySQL ID.
     |      
     |      Raises ProgrammingError when character set is not supported.
     |      
     |      Returns a tuple.
     |  
     |  get_supported() from builtins.type
     |      Retrieves a list with names of all supproted character sets
     |      
     |      Returns a tuple.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  desc = [None, ('big5', 'big5_chinese_ci', True), ('latin2', 'latin2_cz...
     |  
     |  slash_charsets = (1, 13, 28, 84, 87, 88)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from _Constants:
     |  
     |  get_full_info() from builtins.type
     |      get full information about given constant
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from _Constants:
     |  
     |  __new__(cls)
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _Constants:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from _Constants:
     |  
     |  prefix = ''
    
    class ClientFlag(_Flags)
     |  MySQL Client Flags
     |  
     |  Client options as found in the MySQL sources mysql-src/include/mysql_com.h
     |  
     |  Method resolution order:
     |      ClientFlag
     |      _Flags
     |      _Constants
     |      builtins.object
     |  
     |  Class methods defined here:
     |  
     |  get_default() from builtins.type
     |      Get the default client options set
     |      
     |      Returns a flag with all the default client options set
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  CAN_HANDLE_EXPIRED_PASSWORDS = 4194304
     |  
     |  COMPRESS = 32
     |  
     |  CONNECT_ARGS = 1048576
     |  
     |  CONNECT_WITH_DB = 8
     |  
     |  DEPRECATE_EOF = 16777216
     |  
     |  FOUND_ROWS = 2
     |  
     |  IGNORE_SIGPIPE = 4096
     |  
     |  IGNORE_SPACE = 256
     |  
     |  INTERACTIVE = 1024
     |  
     |  LOCAL_FILES = 128
     |  
     |  LONG_FLAG = 4
     |  
     |  LONG_PASSWD = 1
     |  
     |  MULTI_RESULTS = 131072
     |  
     |  MULTI_STATEMENTS = 65536
     |  
     |  NO_SCHEMA = 16
     |  
     |  ODBC = 64
     |  
     |  PLUGIN_AUTH = 524288
     |  
     |  PLUGIN_AUTH_LENENC_CLIENT_DATA = 2097152
     |  
     |  PROTOCOL_41 = 512
     |  
     |  PS_MULTI_RESULTS = 262144
     |  
     |  REMEMBER_OPTIONS = 2147483648
     |  
     |  RESERVED = 16384
     |  
     |  SECURE_CONNECTION = 32768
     |  
     |  SESION_TRACK = 8388608
     |  
     |  SSL = 2048
     |  
     |  SSL_VERIFY_SERVER_CERT = 1073741824
     |  
     |  TRANSACTIONS = 8192
     |  
     |  default = [1, 4, 8, 512, 8192, 32768, 65536, 131072, 128]
     |  
     |  desc = {'CAN_HANDLE_EXPIRED_PASSWORDS': (4194304, "Don't close the con...
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from _Flags:
     |  
     |  get_bit_info(value) from builtins.type
     |      Get the name of all bits set
     |      
     |      Returns a list of strings.
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from _Constants:
     |  
     |  get_desc(name) from builtins.type
     |      Get description of given constant
     |  
     |  get_full_info() from builtins.type
     |      get full information about given constant
     |  
     |  get_info(setid) from builtins.type
     |      Get information about given constant
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from _Constants:
     |  
     |  __new__(cls)
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _Constants:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from _Constants:
     |  
     |  prefix = ''
    
    class DataError(DatabaseError)
     |  Exception for errors reporting problems with processed data
     |  
     |  Method resolution order:
     |      DataError
     |      DatabaseError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods inherited from Error:
     |  
     |  __init__(self, msg=None, errno=None, values=None, sqlstate=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Error:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class DatabaseError(Error)
     |  Exception for errors related to the database
     |  
     |  Method resolution order:
     |      DatabaseError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods inherited from Error:
     |  
     |  __init__(self, msg=None, errno=None, values=None, sqlstate=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Error:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    Date = class date(builtins.object)
     |  date(year, month, day) --> date object
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __format__(...)
     |      Formats self with strftime.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  ctime(...)
     |      Return ctime() style string.
     |  
     |  fromordinal(...) from builtins.type
     |      int -> date corresponding to a proleptic Gregorian ordinal.
     |  
     |  fromtimestamp(...) from builtins.type
     |      timestamp -> local date from a POSIX timestamp (like time.time()).
     |  
     |  isocalendar(...)
     |      Return a 3-tuple containing ISO year, week number, and weekday.
     |  
     |  isoformat(...)
     |      Return string in ISO 8601 format, YYYY-MM-DD.
     |  
     |  isoweekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 1 ... Sunday == 7
     |  
     |  replace(...)
     |      Return date with new specified fields.
     |  
     |  strftime(...)
     |      format -> strftime() style string.
     |  
     |  timetuple(...)
     |      Return time tuple, compatible with time.localtime().
     |  
     |  today(...) from builtins.type
     |      Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).
     |  
     |  toordinal(...)
     |      Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.
     |  
     |  weekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 0 ... Sunday == 6
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  day
     |  
     |  month
     |  
     |  year
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  max = datetime.date(9999, 12, 31)
     |  
     |  min = datetime.date(1, 1, 1)
     |  
     |  resolution = datetime.timedelta(1)
    
    class Error(builtins.Exception)
     |  Exception that is base class for all other error exceptions
     |  
     |  Method resolution order:
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, msg=None, errno=None, values=None, sqlstate=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class FieldFlag(_Flags)
     |  MySQL Field Flags
     |  
     |  Field flags as found in MySQL sources mysql-src/include/mysql_com.h
     |  
     |  Method resolution order:
     |      FieldFlag
     |      _Flags
     |      _Constants
     |      builtins.object
     |  
     |  Data and other attributes defined here:
     |  
     |  AUTO_INCREMENT = 512
     |  
     |  BINARY = 128
     |  
     |  BINCMP = 131072
     |  
     |  BLOB = 16
     |  
     |  ENUM = 256
     |  
     |  FIELD_IN_ADD_INDEX = 1048576
     |  
     |  FIELD_IN_PART_FUNC = 524288
     |  
     |  FIELD_IS_RENAMED = 2097152
     |  
     |  GET_FIXED_FIELDS = 262144
     |  
     |  GROUP = 16384
     |  
     |  MULTIPLE_KEY = 8
     |  
     |  NOT_NULL = 1
     |  
     |  NO_DEFAULT_VALUE = 4096
     |  
     |  NUM = 16384
     |  
     |  ON_UPDATE_NOW = 8192
     |  
     |  PART_KEY = 32768
     |  
     |  PRI_KEY = 2
     |  
     |  SET = 2048
     |  
     |  TIMESTAMP = 1024
     |  
     |  UNIQUE = 65536
     |  
     |  UNIQUE_KEY = 4
     |  
     |  UNSIGNED = 32
     |  
     |  ZEROFILL = 64
     |  
     |  desc = {'AUTO_INCREMENT': (512, 'field is a autoincrement field'), 'BI...
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from _Flags:
     |  
     |  get_bit_info(value) from builtins.type
     |      Get the name of all bits set
     |      
     |      Returns a list of strings.
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from _Constants:
     |  
     |  get_desc(name) from builtins.type
     |      Get description of given constant
     |  
     |  get_full_info() from builtins.type
     |      get full information about given constant
     |  
     |  get_info(setid) from builtins.type
     |      Get information about given constant
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from _Constants:
     |  
     |  __new__(cls)
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _Constants:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from _Constants:
     |  
     |  prefix = ''
    
    class FieldType(_Constants)
     |  MySQL Field Types
     |  
     |  Method resolution order:
     |      FieldType
     |      _Constants
     |      builtins.object
     |  
     |  Class methods defined here:
     |  
     |  get_binary_types() from builtins.type
     |      Get the list of all binary types
     |  
     |  get_number_types() from builtins.type
     |      Get the list of all number types
     |  
     |  get_string_types() from builtins.type
     |      Get the list of all string types
     |  
     |  get_timestamp_types() from builtins.type
     |      Get the list of all timestamp types
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  BIT = 16
     |  
     |  BLOB = 252
     |  
     |  DATE = 10
     |  
     |  DATETIME = 12
     |  
     |  DECIMAL = 0
     |  
     |  DOUBLE = 5
     |  
     |  ENUM = 247
     |  
     |  FLOAT = 4
     |  
     |  GEOMETRY = 255
     |  
     |  INT24 = 9
     |  
     |  JSON = 245
     |  
     |  LONG = 3
     |  
     |  LONGLONG = 8
     |  
     |  LONG_BLOB = 251
     |  
     |  MEDIUM_BLOB = 250
     |  
     |  NEWDATE = 14
     |  
     |  NEWDECIMAL = 246
     |  
     |  NULL = 6
     |  
     |  SET = 248
     |  
     |  SHORT = 2
     |  
     |  STRING = 254
     |  
     |  TIME = 11
     |  
     |  TIMESTAMP = 7
     |  
     |  TINY = 1
     |  
     |  TINY_BLOB = 249
     |  
     |  VARCHAR = 15
     |  
     |  VAR_STRING = 253
     |  
     |  YEAR = 13
     |  
     |  desc = {'BIT': (16, 'BIT'), 'BLOB': (252, 'BLOB'), 'DATE': (10, 'DATE'...
     |  
     |  prefix = 'FIELD_TYPE_'
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from _Constants:
     |  
     |  get_desc(name) from builtins.type
     |      Get description of given constant
     |  
     |  get_full_info() from builtins.type
     |      get full information about given constant
     |  
     |  get_info(setid) from builtins.type
     |      Get information about given constant
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from _Constants:
     |  
     |  __new__(cls)
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _Constants:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class IntegrityError(DatabaseError)
     |  Exception for errors regarding relational integrity
     |  
     |  Method resolution order:
     |      IntegrityError
     |      DatabaseError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods inherited from Error:
     |  
     |  __init__(self, msg=None, errno=None, values=None, sqlstate=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Error:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class InterfaceError(Error)
     |  Exception for errors related to the interface
     |  
     |  Method resolution order:
     |      InterfaceError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods inherited from Error:
     |  
     |  __init__(self, msg=None, errno=None, values=None, sqlstate=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Error:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class InternalError(DatabaseError)
     |  Exception for errors internal database errors
     |  
     |  Method resolution order:
     |      InternalError
     |      DatabaseError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods inherited from Error:
     |  
     |  __init__(self, msg=None, errno=None, values=None, sqlstate=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Error:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class MySQLConnection(mysql.connector.abstracts.MySQLConnectionAbstract)
     |  Connection to a MySQL Server
     |  
     |  Method resolution order:
     |      MySQLConnection
     |      mysql.connector.abstracts.MySQLConnectionAbstract
     |      mysql.connector.abstracts.MySQLConnectionAbstract
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, *args, **kwargs)
     |      Initialize
     |  
     |  close(self)
     |      Disconnect from the MySQL server
     |  
     |  cmd_change_user(self, username='', password='', database='', charset=45)
     |      Change the current logged in user
     |      
     |      This method allows to change the current logged in user information.
     |      The result is a dictionary with OK packet information.
     |      
     |      Returns a dict()
     |  
     |  cmd_debug(self)
     |      Send the DEBUG command
     |      
     |      This method sends the DEBUG command to the MySQL server, which
     |      requires the MySQL user to have SUPER privilege. The output will go
     |      to the MySQL server error log and the result of this method is a
     |      dictionary with EOF packet information.
     |      
     |      Returns a dict()
     |  
     |  cmd_init_db(self, database)
     |      Change the current database
     |      
     |      This method changes the current (default) database by sending the
     |      INIT_DB command. The result is a dictionary containing the OK packet
     |      information.
     |      
     |      Returns a dict()
     |  
     |  cmd_ping(self)
     |      Send the PING command
     |      
     |      This method sends the PING command to the MySQL server. It is used to
     |      check if the the connection is still valid. The result of this
     |      method is dictionary with OK packet information.
     |      
     |      Returns a dict()
     |  
     |  cmd_process_kill(self, mysql_pid)
     |      Kill a MySQL process
     |      
     |      This method send the PROCESS_KILL command to the server along with
     |      the process ID. The result is a dictionary with the OK packet
     |      information.
     |      
     |      Returns a dict()
     |  
     |  cmd_query(self, query, raw=False, buffered=False, raw_as_string=False)
     |      Send a query to the MySQL server
     |      
     |      This method send the query to the MySQL server and returns the result.
     |      
     |      If there was a text result, a tuple will be returned consisting of
     |      the number of columns and a list containing information about these
     |      columns.
     |      
     |      When the query doesn't return a text result, the OK or EOF packet
     |      information as dictionary will be returned. In case the result was
     |      an error, exception errors.Error will be raised.
     |      
     |      Returns a tuple()
     |  
     |  cmd_query_iter(self, statements)
     |      Send one or more statements to the MySQL server
     |      
     |      Similar to the cmd_query method, but instead returns a generator
     |      object to iterate through results. It sends the statements to the
     |      MySQL server and through the iterator you can get the results.
     |      
     |      statement = 'SELECT 1; INSERT INTO t1 VALUES (); SELECT 2'
     |      for result in cnx.cmd_query(statement, iterate=True):
     |          if 'columns' in result:
     |              columns = result['columns']
     |              rows = cnx.get_rows()
     |          else:
     |              # do something useful with INSERT result
     |      
     |      Returns a generator.
     |  
     |  cmd_quit(self)
     |      Close the current connection with the server
     |      
     |      This method sends the QUIT command to the MySQL server, closing the
     |      current connection. Since the no response can be returned to the
     |      client, cmd_quit() will return the packet it send.
     |      
     |      Returns a str()
     |  
     |  cmd_refresh(self, options)
     |      Send the Refresh command to the MySQL server
     |      
     |      This method sends the Refresh command to the MySQL server. The options
     |      argument should be a bitwise value using constants.RefreshOption.
     |      Usage example:
     |       RefreshOption = mysql.connector.RefreshOption
     |       refresh = RefreshOption.LOG | RefreshOption.THREADS
     |       cnx.cmd_refresh(refresh)
     |      
     |      The result is a dictionary with the OK packet information.
     |      
     |      Returns a dict()
     |  
     |  cmd_reset_connection(self)
     |      Resets the session state without re-authenticating
     |      
     |      Works only for MySQL server 5.7.3 or later.
     |      The result is a dictionary with OK packet information.
     |      
     |      Returns a dict()
     |  
     |  cmd_shutdown(self, shutdown_type=None)
     |      Shut down the MySQL Server
     |      
     |      This method sends the SHUTDOWN command to the MySQL server and is only
     |      possible if the current user has SUPER privileges. The result is a
     |      dictionary containing the OK packet information.
     |      
     |      Note: Most applications and scripts do not the SUPER privilege.
     |      
     |      Returns a dict()
     |  
     |  cmd_statistics(self)
     |      Send the statistics command to the MySQL Server
     |      
     |      This method sends the STATISTICS command to the MySQL server. The
     |      result is a dictionary with various statistical information.
     |      
     |      Returns a dict()
     |  
     |  cmd_stmt_close(self, statement_id)
     |      Deallocate a prepared MySQL statement
     |      
     |      This method deallocates the prepared statement using the
     |      statement_id. Note that the MySQL server does not return
     |      anything.
     |  
     |  cmd_stmt_execute(self, statement_id, data=(), parameters=(), flags=0)
     |      Execute a prepared MySQL statement
     |  
     |  cmd_stmt_fetch(self, statement_id, rows=1)
     |      Fetch a MySQL statement Result Set
     |      
     |      This method will send the FETCH command to MySQL together with the
     |      given statement id and the number of rows to fetch.
     |  
     |  cmd_stmt_prepare(self, statement)
     |      Prepare a MySQL statement
     |      
     |      This method will send the PREPARE command to MySQL together with the
     |      given statement.
     |      
     |      Returns a dict()
     |  
     |  cmd_stmt_reset(self, statement_id)
     |      Reset data for prepared statement sent as long data
     |      
     |      The result is a dictionary with OK packet information.
     |      
     |      Returns a dict()
     |  
     |  cmd_stmt_send_long_data(self, statement_id, param_id, data)
     |      Send data for a column
     |      
     |      This methods send data for a column (for example BLOB) for statement
     |      identified by statement_id. The param_id indicate which parameter
     |      the data belongs too.
     |      The data argument should be a file-like object.
     |      
     |      Since MySQL does not send anything back, no error is raised. When
     |      the MySQL server is not reachable, an OperationalError is raised.
     |      
     |      cmd_stmt_send_long_data should be called before cmd_stmt_execute.
     |      
     |      The total bytes send is returned.
     |      
     |      Returns int.
     |  
     |  commit(self)
     |      Commit current transaction
     |  
     |  consume_results(self)
     |      Consume results
     |  
     |  cursor(self, buffered=None, raw=None, prepared=None, cursor_class=None, dictionary=None, named_tuple=None)
     |      Instantiates and returns a cursor
     |      
     |      By default, MySQLCursor is returned. Depending on the options
     |      while connecting, a buffered and/or raw cursor is instantiated
     |      instead. Also depending upon the cursor options, rows can be
     |      returned as dictionary or named tuple.
     |      
     |      Dictionary and namedtuple based cursors are available with buffered
     |      output but not raw.
     |      
     |      It is possible to also give a custom cursor through the
     |      cursor_class parameter, but it needs to be a subclass of
     |      mysql.connector.cursor.CursorBase.
     |      
     |      Raises ProgrammingError when cursor_class is not a subclass of
     |      CursorBase. Raises ValueError when cursor is not available.
     |      
     |      Returns a cursor-object
     |  
     |  disconnect = close(self)
     |  
     |  get_row(self, binary=False, columns=None, raw=None)
     |      Get the next rows returned by the MySQL server
     |      
     |      This method gets one row from the result set after sending, for
     |      example, the query command. The result is a tuple consisting of the
     |      row and the EOF packet.
     |      If no row was available in the result set, the row data will be None.
     |      
     |      Returns a tuple.
     |  
     |  get_rows(self, count=None, binary=False, columns=None, raw=None)
     |      Get all rows returned by the MySQL server
     |      
     |      This method gets all rows returned by the MySQL server after sending,
     |      for example, the query command. The result is a tuple consisting of
     |      a list of rows and the EOF packet.
     |      
     |      Returns a tuple()
     |  
     |  handle_unread_result(self)
     |      Check whether there is an unread result
     |  
     |  info_query(self, query)
     |      Send a query which only returns 1 row
     |  
     |  is_connected(self)
     |      Reports whether the connection to MySQL Server is available
     |      
     |      This method checks whether the connection to MySQL is available.
     |      It is similar to ping(), but unlike the ping()-method, either True
     |      or False is returned and no exception is raised.
     |      
     |      Returns True or False.
     |  
     |  ping(self, reconnect=False, attempts=1, delay=0)
     |      Check availability of the MySQL server
     |      
     |      When reconnect is set to True, one or more attempts are made to try
     |      to reconnect to the MySQL server using the reconnect()-method.
     |      
     |      delay is the number of seconds to wait between each retry.
     |      
     |      When the connection is not available, an InterfaceError is raised. Use
     |      the is_connected()-method if you just want to check the connection
     |      without raising an error.
     |      
     |      Raises InterfaceError on errors.
     |  
     |  reconnect(self, attempts=1, delay=0)
     |      Attempt to reconnect to the MySQL server
     |      
     |      The argument attempts should be the number of times a reconnect
     |      is tried. The delay argument is the number of seconds to wait between
     |      each retry.
     |      
     |      You may want to set the number of attempts higher and use delay when
     |      you expect the MySQL server to be down for maintenance or when you
     |      expect the network to be temporary unavailable.
     |      
     |      Raises InterfaceError on errors.
     |  
     |  reset_session(self, user_variables=None, session_variables=None)
     |      Clears the current active session
     |      
     |      This method resets the session state, if the MySQL server is 5.7.3
     |      or later active session will be reset without re-authenticating.
     |      For other server versions session will be reset by re-authenticating.
     |      
     |      It is possible to provide a sequence of variables and their values to
     |      be set after clearing the session. This is possible for both user
     |      defined variables and session variables.
     |      This method takes two arguments user_variables and session_variables
     |      which are dictionaries.
     |      
     |      Raises OperationalError if not connected, InternalError if there are
     |      unread results and InterfaceError on errors.
     |  
     |  rollback(self)
     |      Rollback current transaction
     |  
     |  shutdown(self)
     |      Shut down connection to MySQL Server.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  connection_id
     |      MySQL connection ID
     |  
     |  database
     |      Get the current database
     |  
     |  in_transaction
     |      MySQL session has started a transaction
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __abstractmethods__ = frozenset()
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from mysql.connector.abstracts.MySQLConnectionAbstract:
     |  
     |  cmd_process_info(self)
     |      Get the process list of the MySQL Server
     |      
     |      This method is a placeholder to notify that the PROCESS_INFO command
     |      is not supported by raising the NotSupportedError. The command
     |      "SHOW PROCESSLIST" should be send using the cmd_query()-method or
     |      using the INFORMATION_SCHEMA database.
     |      
     |      Raises NotSupportedError exception
     |  
     |  config(self, **kwargs)
     |      Configure the MySQL Connection
     |      
     |      This method allows you to configure the MySQLConnection instance.
     |      
     |      Raises on errors.
     |  
     |  connect(self, **kwargs)
     |      Connect to the MySQL server
     |      
     |      This method sets up the connection to the MySQL server. If no
     |      arguments are given, it will use the already configured or default
     |      values.
     |  
     |  get_server_info(self)
     |      Get the original MySQL version information
     |      
     |      This method returns the original MySQL server as text. If not
     |      previously connected, it will return None.
     |      
     |      Returns a string or None.
     |  
     |  get_server_version(self)
     |      Get the MySQL version
     |      
     |      This method returns the MySQL server version as a tuple. If not
     |      previously connected, it will return None.
     |      
     |      Returns a tuple or None.
     |  
     |  isset_client_flag(self, flag)
     |      Check if a client flag is set
     |  
     |  set_charset_collation(self, charset=None, collation=None)
     |      Sets the character set and collation for the current connection
     |      
     |      This method sets the character set and collation to be used for
     |      the current connection. The charset argument can be either the
     |      name of a character set as a string, or the numerical equivalent
     |      as defined in constants.CharacterSet.
     |      
     |      When the collation is not given, the default will be looked up and
     |      used.
     |      
     |      For example, the following will set the collation for the latin1
     |      character set to latin1_general_ci:
     |      
     |         set_charset('latin1','latin1_general_ci')
     |  
     |  set_client_flags(self, flags)
     |      Set the client flags
     |      
     |      The flags-argument can be either an int or a list (or tuple) of
     |      ClientFlag-values. If it is an integer, it will set client_flags
     |      to flags as is.
     |      If flags is a list (or tuple), each flag will be set or unset
     |      when it's negative.
     |      
     |      set_client_flags([ClientFlag.FOUND_ROWS,-ClientFlag.LONG_FLAG])
     |      
     |      Raises ProgrammingError when the flags argument is not a set or
     |      an integer bigger than 0.
     |      
     |      Returns self.client_flags
     |  
     |  set_converter_class(self, convclass)
     |      Set the converter class to be used. This should be a class overloading
     |      methods and members of conversion.MySQLConverter.
     |  
     |  set_login(self, username=None, password=None)
     |      Set login information for MySQL
     |      
     |      Set the username and/or password for the user connecting to
     |      the MySQL Server.
     |  
     |  set_unicode(self, value=True)
     |      Toggle unicode mode
     |      
     |      Set whether we return string fields as unicode or not.
     |      Default is True.
     |  
     |  start_transaction(self, consistent_snapshot=False, isolation_level=None, readonly=None)
     |      Start a transaction
     |      
     |      This method explicitly starts a transaction sending the
     |      START TRANSACTION statement to the MySQL server. You can optionally
     |      set whether there should be a consistent snapshot, which
     |      isolation level you need or which access mode i.e. READ ONLY or
     |      READ WRITE.
     |      
     |      For example, to start a transaction with isolation level SERIALIZABLE,
     |      you would do the following:
     |          >>> cnx = mysql.connector.connect(..)
     |          >>> cnx.start_transaction(isolation_level='SERIALIZABLE')
     |      
     |      Raises ProgrammingError when a transaction is already in progress
     |      and when ValueError when isolation_level specifies an Unknown
     |      level.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from mysql.connector.abstracts.MySQLConnectionAbstract:
     |  
     |  autocommit
     |      Get whether autocommit is on or off
     |  
     |  can_consume_results
     |      Returns whether to consume results
     |  
     |  charset
     |      Returns the character set for current connection
     |      
     |      This property returns the character set name of the current connection.
     |      The server is queried when the connection is active. If not connected,
     |      the configured character set name is returned.
     |      
     |      Returns a string.
     |  
     |  collation
     |      Returns the collation for current connection
     |      
     |      This property returns the collation name of the current connection.
     |      The server is queried when the connection is active. If not connected,
     |      the configured collation name is returned.
     |      
     |      Returns a string.
     |  
     |  get_warnings
     |      Get whether this connection retrieves warnings automatically
     |      
     |      This method returns whether this connection retrieves warnings
     |      automatically.
     |      
     |      Returns True, or False when warnings are not retrieved.
     |  
     |  python_charset
     |      Returns the Python character set for current connection
     |      
     |      This property returns the character set name of the current connection.
     |      Note that, unlike property charset, this checks if the previously set
     |      character set is supported by Python and if not, it returns the
     |      equivalent character set that Python supports.
     |      
     |      Returns a string.
     |  
     |  raise_on_warnings
     |      Get whether this connection raises an error on warnings
     |      
     |      This method returns whether this connection will raise errors when
     |      MySQL reports warnings.
     |      
     |      Returns True or False.
     |  
     |  server_host
     |      MySQL server IP address or name
     |  
     |  server_port
     |      MySQL server TCP/IP port
     |  
     |  sql_mode
     |      Get the SQL mode
     |  
     |  time_zone
     |      Get the current time zone
     |  
     |  unix_socket
     |      MySQL Unix socket file location
     |  
     |  unread_result
     |      Get whether there is an unread result
     |      
     |      This method is used by cursors to check whether another cursor still
     |      needs to retrieve its result set.
     |      
     |      Returns True, or False when there is no unread result.
     |  
     |  user
     |      User used while connecting to MySQL
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from mysql.connector.abstracts.MySQLConnectionAbstract:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class NotSupportedError(DatabaseError)
     |  Exception for errors when an unsupported database feature was used
     |  
     |  Method resolution order:
     |      NotSupportedError
     |      DatabaseError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods inherited from Error:
     |  
     |  __init__(self, msg=None, errno=None, values=None, sqlstate=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Error:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class OperationalError(DatabaseError)
     |  Exception for errors related to the database's operation
     |  
     |  Method resolution order:
     |      OperationalError
     |      DatabaseError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods inherited from Error:
     |  
     |  __init__(self, msg=None, errno=None, values=None, sqlstate=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Error:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class ProgrammingError(DatabaseError)
     |  Exception for errors programming errors
     |  
     |  Method resolution order:
     |      ProgrammingError
     |      DatabaseError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods inherited from Error:
     |  
     |  __init__(self, msg=None, errno=None, values=None, sqlstate=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Error:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class RefreshOption(_Constants)
     |  MySQL Refresh command options
     |  
     |  Options used when sending the COM_REFRESH server command.
     |  
     |  Method resolution order:
     |      RefreshOption
     |      _Constants
     |      builtins.object
     |  
     |  Data and other attributes defined here:
     |  
     |  GRANT = 1
     |  
     |  HOST = 8
     |  
     |  LOG = 2
     |  
     |  SLAVE = 64
     |  
     |  STATUS = 16
     |  
     |  TABLES = 4
     |  
     |  THREADS = 32
     |  
     |  desc = {'GRANT': (1, 'Refresh grant tables'), 'HOSTS': (8, 'Flush host...
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from _Constants:
     |  
     |  get_desc(name) from builtins.type
     |      Get description of given constant
     |  
     |  get_full_info() from builtins.type
     |      get full information about given constant
     |  
     |  get_info(setid) from builtins.type
     |      Get information about given constant
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from _Constants:
     |  
     |  __new__(cls)
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _Constants:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from _Constants:
     |  
     |  prefix = ''
    
    Time = class time(builtins.object)
     |  time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object
     |  
     |  All arguments are optional. tzinfo may be None, or an instance of
     |  a tzinfo subclass. The remaining arguments may be ints.
     |  
     |  Methods defined here:
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __format__(...)
     |      Formats self with strftime.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |  
     |  __reduce_ex__(...)
     |      __reduce_ex__(proto) -> (cls, state)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  dst(...)
     |      Return self.tzinfo.dst(self).
     |  
     |  isoformat(...)
     |      Return string in ISO 8601 format, [HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].
     |      
     |      timespec specifies what components of the time to include.
     |  
     |  replace(...)
     |      Return time with new specified fields.
     |  
     |  strftime(...)
     |      format -> strftime() style string.
     |  
     |  tzname(...)
     |      Return self.tzinfo.tzname(self).
     |  
     |  utcoffset(...)
     |      Return self.tzinfo.utcoffset(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  fold
     |  
     |  hour
     |  
     |  microsecond
     |  
     |  minute
     |  
     |  second
     |  
     |  tzinfo
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  max = datetime.time(23, 59, 59, 999999)
     |  
     |  min = datetime.time(0, 0)
     |  
     |  resolution = datetime.timedelta(0, 0, 1)
    
    Timestamp = class datetime(date)
     |  datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
     |  
     |  The year, month and day arguments are required. tzinfo may be None, or an
     |  instance of a tzinfo subclass. The remaining arguments may be ints.
     |  
     |  Method resolution order:
     |      datetime
     |      date
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |  
     |  __reduce_ex__(...)
     |      __reduce_ex__(proto) -> (cls, state)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  astimezone(...)
     |      tz -> convert to local time in new timezone tz
     |  
     |  combine(...) from builtins.type
     |      date, time -> datetime with same date and time fields
     |  
     |  ctime(...)
     |      Return ctime() style string.
     |  
     |  date(...)
     |      Return date object with same year, month and day.
     |  
     |  dst(...)
     |      Return self.tzinfo.dst(self).
     |  
     |  fromtimestamp(...) from builtins.type
     |      timestamp[, tz] -> tz's local time from POSIX timestamp.
     |  
     |  isoformat(...)
     |      [sep] -> string in ISO 8601 format, YYYY-MM-DDT[HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].
     |      sep is used to separate the year from the time, and defaults to 'T'.
     |      timespec specifies what components of the time to include (allowed values are 'auto', 'hours', 'minutes', 'seconds', 'milliseconds', and 'microseconds').
     |  
     |  now(tz=None) from builtins.type
     |      Returns new datetime object representing current time local to tz.
     |      
     |        tz
     |          Timezone object.
     |      
     |      If no tz is specified, uses local timezone.
     |  
     |  replace(...)
     |      Return datetime with new specified fields.
     |  
     |  strptime(...) from builtins.type
     |      string, format -> new datetime parsed from a string (like time.strptime()).
     |  
     |  time(...)
     |      Return time object with same time but with tzinfo=None.
     |  
     |  timestamp(...)
     |      Return POSIX timestamp as float.
     |  
     |  timetuple(...)
     |      Return time tuple, compatible with time.localtime().
     |  
     |  timetz(...)
     |      Return time object with same time and tzinfo.
     |  
     |  tzname(...)
     |      Return self.tzinfo.tzname(self).
     |  
     |  utcfromtimestamp(...) from builtins.type
     |      Construct a naive UTC datetime from a POSIX timestamp.
     |  
     |  utcnow(...) from builtins.type
     |      Return a new datetime representing UTC day and time.
     |  
     |  utcoffset(...)
     |      Return self.tzinfo.utcoffset(self).
     |  
     |  utctimetuple(...)
     |      Return UTC time tuple, compatible with time.localtime().
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  fold
     |  
     |  hour
     |  
     |  microsecond
     |  
     |  minute
     |  
     |  second
     |  
     |  tzinfo
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  max = datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
     |  
     |  min = datetime.datetime(1, 1, 1, 0, 0)
     |  
     |  resolution = datetime.timedelta(0, 0, 1)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from date:
     |  
     |  __format__(...)
     |      Formats self with strftime.
     |  
     |  fromordinal(...) from builtins.type
     |      int -> date corresponding to a proleptic Gregorian ordinal.
     |  
     |  isocalendar(...)
     |      Return a 3-tuple containing ISO year, week number, and weekday.
     |  
     |  isoweekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 1 ... Sunday == 7
     |  
     |  strftime(...)
     |      format -> strftime() style string.
     |  
     |  today(...) from builtins.type
     |      Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).
     |  
     |  toordinal(...)
     |      Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.
     |  
     |  weekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 0 ... Sunday == 6
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from date:
     |  
     |  day
     |  
     |  month
     |  
     |  year
    
    class Warning(builtins.Exception)
     |  Exception for important warnings
     |  
     |  Method resolution order:
     |      Warning
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args

FUNCTIONS
    Connect = connect(*args, **kwargs)
        Create or get a MySQL connection object
        
        In its simpliest form, Connect() will open a connection to a
        MySQL server and return a MySQLConnection object.
        
        When any connection pooling arguments are given, for example pool_name
        or pool_size, a pool is created or a previously one is used to return
        a PooledMySQLConnection.
        
        Returns MySQLConnection or PooledMySQLConnection.
    
    DateFromTicks(ticks)
    
    TimeFromTicks(ticks)
    
    TimestampFromTicks(ticks)
    
    connect(*args, **kwargs)
        Create or get a MySQL connection object
        
        In its simpliest form, Connect() will open a connection to a
        MySQL server and return a MySQLConnection object.
        
        When any connection pooling arguments are given, for example pool_name
        or pool_size, a pool is created or a previously one is used to return
        a PooledMySQLConnection.
        
        Returns MySQLConnection or PooledMySQLConnection.
    
    custom_error_exception(error=None, exception=None)
        Define custom exceptions for MySQL server errors
        
        This function defines custom exceptions for MySQL server errors and
        returns the current set customizations.
        
        If error is a MySQL Server error number, then you have to pass also the
        exception class.
        
        The error argument can also be a dictionary in which case the key is
        the server error number, and value the exception to be raised.
        
        If none of the arguments are given, then custom_error_exception() will
        simply return the current set customizations.
        
        To reset the customizations, simply supply an empty dictionary.
        
        Examples:
            import mysql.connector
            from mysql.connector import errorcode
        
            # Server error 1028 should raise a DatabaseError
            mysql.connector.custom_error_exception(
                1028, mysql.connector.DatabaseError)
        
            # Or using a dictionary:
            mysql.connector.custom_error_exception({
                1028: mysql.connector.DatabaseError,
                1029: mysql.connector.OperationalError,
                })
        
            # Reset
            mysql.connector.custom_error_exception({})
        
        Returns a dictionary.

DATA
    BINARY = <mysql.connector.dbapi._DBAPITypeObject object>
    DATETIME = <mysql.connector.dbapi._DBAPITypeObject object>
    HAVE_CEXT = True
    NUMBER = <mysql.connector.dbapi._DBAPITypeObject object>
    ROWID = <mysql.connector.dbapi._DBAPITypeObject object>
    STRING = <mysql.connector.dbapi._DBAPITypeObject object>
    __all__ = ['MySQLConnection', 'Connect', 'custom_error_exception', 'Fi...
    __version_info__ = (8, 0, 12, '', 1)
    apilevel = '2.0'
    paramstyle = 'pyformat'
    threadsafety = 1

VERSION
    8.0.12

FILE
    /usr/local/lib/python3.6/site-packages/mysql/connector/__init__.py


[Finished in 0.6s]