// ORM class for table 'plan_eatplace'
// WARNING: This class is AUTO-GENERATED. Modify at your own risk.
//
// Debug information:
// Generated date: Thu Feb 16 15:07:39 KST 2023
// For connector: org.apache.sqoop.manager.MySQLManager
import org.apache.hadoop.io.BytesWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.Writable;
import org.apache.hadoop.mapred.lib.db.DBWritable;
import com.cloudera.sqoop.lib.JdbcWritableBridge;
import com.cloudera.sqoop.lib.DelimiterSet;
import com.cloudera.sqoop.lib.FieldFormatter;
import com.cloudera.sqoop.lib.RecordParser;
import com.cloudera.sqoop.lib.BooleanParser;
import com.cloudera.sqoop.lib.BlobRef;
import com.cloudera.sqoop.lib.ClobRef;
import com.cloudera.sqoop.lib.LargeObjectLoader;
import com.cloudera.sqoop.lib.SqoopRecord;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.sql.Date;
import java.sql.Time;
import java.sql.Timestamp;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

public class plan_eatplace extends SqoopRecord  implements DBWritable, Writable {
  private final int PROTOCOL_VERSION = 3;
  public int getClassFormatVersion() { return PROTOCOL_VERSION; }
  public static interface FieldSetterCommand {    void setField(Object value);  }  protected ResultSet __cur_result_set;
  private Map<String, FieldSetterCommand> setters = new HashMap<String, FieldSetterCommand>();
  private void init0() {
    setters.put("address", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        plan_eatplace.this.address = (String)value;
      }
    });
    setters.put("gu", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        plan_eatplace.this.gu = (String)value;
      }
    });
    setters.put("name", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        plan_eatplace.this.name = (String)value;
      }
    });
    setters.put("no", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        plan_eatplace.this.no = (Integer)value;
      }
    });
    setters.put("review_star", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        plan_eatplace.this.review_star = (String)value;
      }
    });
    setters.put("review_text", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        plan_eatplace.this.review_text = (String)value;
      }
    });
  }
  public plan_eatplace() {
    init0();
  }
  private String address;
  public String get_address() {
    return address;
  }
  public void set_address(String address) {
    this.address = address;
  }
  public plan_eatplace with_address(String address) {
    this.address = address;
    return this;
  }
  private String gu;
  public String get_gu() {
    return gu;
  }
  public void set_gu(String gu) {
    this.gu = gu;
  }
  public plan_eatplace with_gu(String gu) {
    this.gu = gu;
    return this;
  }
  private String name;
  public String get_name() {
    return name;
  }
  public void set_name(String name) {
    this.name = name;
  }
  public plan_eatplace with_name(String name) {
    this.name = name;
    return this;
  }
  private Integer no;
  public Integer get_no() {
    return no;
  }
  public void set_no(Integer no) {
    this.no = no;
  }
  public plan_eatplace with_no(Integer no) {
    this.no = no;
    return this;
  }
  private String review_star;
  public String get_review_star() {
    return review_star;
  }
  public void set_review_star(String review_star) {
    this.review_star = review_star;
  }
  public plan_eatplace with_review_star(String review_star) {
    this.review_star = review_star;
    return this;
  }
  private String review_text;
  public String get_review_text() {
    return review_text;
  }
  public void set_review_text(String review_text) {
    this.review_text = review_text;
  }
  public plan_eatplace with_review_text(String review_text) {
    this.review_text = review_text;
    return this;
  }
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (!(o instanceof plan_eatplace)) {
      return false;
    }
    plan_eatplace that = (plan_eatplace) o;
    boolean equal = true;
    equal = equal && (this.address == null ? that.address == null : this.address.equals(that.address));
    equal = equal && (this.gu == null ? that.gu == null : this.gu.equals(that.gu));
    equal = equal && (this.name == null ? that.name == null : this.name.equals(that.name));
    equal = equal && (this.no == null ? that.no == null : this.no.equals(that.no));
    equal = equal && (this.review_star == null ? that.review_star == null : this.review_star.equals(that.review_star));
    equal = equal && (this.review_text == null ? that.review_text == null : this.review_text.equals(that.review_text));
    return equal;
  }
  public boolean equals0(Object o) {
    if (this == o) {
      return true;
    }
    if (!(o instanceof plan_eatplace)) {
      return false;
    }
    plan_eatplace that = (plan_eatplace) o;
    boolean equal = true;
    equal = equal && (this.address == null ? that.address == null : this.address.equals(that.address));
    equal = equal && (this.gu == null ? that.gu == null : this.gu.equals(that.gu));
    equal = equal && (this.name == null ? that.name == null : this.name.equals(that.name));
    equal = equal && (this.no == null ? that.no == null : this.no.equals(that.no));
    equal = equal && (this.review_star == null ? that.review_star == null : this.review_star.equals(that.review_star));
    equal = equal && (this.review_text == null ? that.review_text == null : this.review_text.equals(that.review_text));
    return equal;
  }
  public void readFields(ResultSet __dbResults) throws SQLException {
    this.__cur_result_set = __dbResults;
    this.address = JdbcWritableBridge.readString(1, __dbResults);
    this.gu = JdbcWritableBridge.readString(2, __dbResults);
    this.name = JdbcWritableBridge.readString(3, __dbResults);
    this.no = JdbcWritableBridge.readInteger(4, __dbResults);
    this.review_star = JdbcWritableBridge.readString(5, __dbResults);
    this.review_text = JdbcWritableBridge.readString(6, __dbResults);
  }
  public void readFields0(ResultSet __dbResults) throws SQLException {
    this.address = JdbcWritableBridge.readString(1, __dbResults);
    this.gu = JdbcWritableBridge.readString(2, __dbResults);
    this.name = JdbcWritableBridge.readString(3, __dbResults);
    this.no = JdbcWritableBridge.readInteger(4, __dbResults);
    this.review_star = JdbcWritableBridge.readString(5, __dbResults);
    this.review_text = JdbcWritableBridge.readString(6, __dbResults);
  }
  public void loadLargeObjects(LargeObjectLoader __loader)
      throws SQLException, IOException, InterruptedException {
  }
  public void loadLargeObjects0(LargeObjectLoader __loader)
      throws SQLException, IOException, InterruptedException {
  }
  public void write(PreparedStatement __dbStmt) throws SQLException {
    write(__dbStmt, 0);
  }

  public int write(PreparedStatement __dbStmt, int __off) throws SQLException {
    JdbcWritableBridge.writeString(address, 1 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(gu, 2 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(name, 3 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeInteger(no, 4 + __off, 4, __dbStmt);
    JdbcWritableBridge.writeString(review_star, 5 + __off, -1, __dbStmt);
    JdbcWritableBridge.writeString(review_text, 6 + __off, -1, __dbStmt);
    return 6;
  }
  public void write0(PreparedStatement __dbStmt, int __off) throws SQLException {
    JdbcWritableBridge.writeString(address, 1 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(gu, 2 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(name, 3 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeInteger(no, 4 + __off, 4, __dbStmt);
    JdbcWritableBridge.writeString(review_star, 5 + __off, -1, __dbStmt);
    JdbcWritableBridge.writeString(review_text, 6 + __off, -1, __dbStmt);
  }
  public void readFields(DataInput __dataIn) throws IOException {
this.readFields0(__dataIn);  }
  public void readFields0(DataInput __dataIn) throws IOException {
    if (__dataIn.readBoolean()) { 
        this.address = null;
    } else {
    this.address = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.gu = null;
    } else {
    this.gu = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.name = null;
    } else {
    this.name = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.no = null;
    } else {
    this.no = Integer.valueOf(__dataIn.readInt());
    }
    if (__dataIn.readBoolean()) { 
        this.review_star = null;
    } else {
    this.review_star = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.review_text = null;
    } else {
    this.review_text = Text.readString(__dataIn);
    }
  }
  public void write(DataOutput __dataOut) throws IOException {
    if (null == this.address) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, address);
    }
    if (null == this.gu) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, gu);
    }
    if (null == this.name) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, name);
    }
    if (null == this.no) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeInt(this.no);
    }
    if (null == this.review_star) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, review_star);
    }
    if (null == this.review_text) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, review_text);
    }
  }
  public void write0(DataOutput __dataOut) throws IOException {
    if (null == this.address) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, address);
    }
    if (null == this.gu) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, gu);
    }
    if (null == this.name) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, name);
    }
    if (null == this.no) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeInt(this.no);
    }
    if (null == this.review_star) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, review_star);
    }
    if (null == this.review_text) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, review_text);
    }
  }
  private static final DelimiterSet __outputDelimiters = new DelimiterSet((char) 44, (char) 10, (char) 0, (char) 0, false);
  public String toString() {
    return toString(__outputDelimiters, true);
  }
  public String toString(DelimiterSet delimiters) {
    return toString(delimiters, true);
  }
  public String toString(boolean useRecordDelim) {
    return toString(__outputDelimiters, useRecordDelim);
  }
  public String toString(DelimiterSet delimiters, boolean useRecordDelim) {
    StringBuilder __sb = new StringBuilder();
    char fieldDelim = delimiters.getFieldsTerminatedBy();
    __sb.append(FieldFormatter.escapeAndEnclose(address==null?"null":address, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(gu==null?"null":gu, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(name==null?"null":name, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(no==null?"null":"" + no, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(review_star==null?"null":review_star, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(review_text==null?"null":review_text, delimiters));
    if (useRecordDelim) {
      __sb.append(delimiters.getLinesTerminatedBy());
    }
    return __sb.toString();
  }
  public void toString0(DelimiterSet delimiters, StringBuilder __sb, char fieldDelim) {
    __sb.append(FieldFormatter.escapeAndEnclose(address==null?"null":address, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(gu==null?"null":gu, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(name==null?"null":name, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(no==null?"null":"" + no, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(review_star==null?"null":review_star, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(review_text==null?"null":review_text, delimiters));
  }
  private static final DelimiterSet __inputDelimiters = new DelimiterSet((char) 44, (char) 10, (char) 0, (char) 0, false);
  private RecordParser __parser;
  public void parse(Text __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(CharSequence __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(byte [] __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(char [] __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(ByteBuffer __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(CharBuffer __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  private void __loadFromFields(List<String> fields) {
    Iterator<String> __it = fields.listIterator();
    String __cur_str = null;
    try {
    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.address = null; } else {
      this.address = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.gu = null; } else {
      this.gu = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.name = null; } else {
      this.name = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.no = null; } else {
      this.no = Integer.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.review_star = null; } else {
      this.review_star = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.review_text = null; } else {
      this.review_text = __cur_str;
    }

    } catch (RuntimeException e) {    throw new RuntimeException("Can't parse input data: '" + __cur_str + "'", e);    }  }

  private void __loadFromFields0(Iterator<String> __it) {
    String __cur_str = null;
    try {
    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.address = null; } else {
      this.address = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.gu = null; } else {
      this.gu = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.name = null; } else {
      this.name = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.no = null; } else {
      this.no = Integer.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.review_star = null; } else {
      this.review_star = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.review_text = null; } else {
      this.review_text = __cur_str;
    }

    } catch (RuntimeException e) {    throw new RuntimeException("Can't parse input data: '" + __cur_str + "'", e);    }  }

  public Object clone() throws CloneNotSupportedException {
    plan_eatplace o = (plan_eatplace) super.clone();
    return o;
  }

  public void clone0(plan_eatplace o) throws CloneNotSupportedException {
  }

  public Map<String, Object> getFieldMap() {
    Map<String, Object> __sqoop$field_map = new HashMap<String, Object>();
    __sqoop$field_map.put("address", this.address);
    __sqoop$field_map.put("gu", this.gu);
    __sqoop$field_map.put("name", this.name);
    __sqoop$field_map.put("no", this.no);
    __sqoop$field_map.put("review_star", this.review_star);
    __sqoop$field_map.put("review_text", this.review_text);
    return __sqoop$field_map;
  }

  public void getFieldMap0(Map<String, Object> __sqoop$field_map) {
    __sqoop$field_map.put("address", this.address);
    __sqoop$field_map.put("gu", this.gu);
    __sqoop$field_map.put("name", this.name);
    __sqoop$field_map.put("no", this.no);
    __sqoop$field_map.put("review_star", this.review_star);
    __sqoop$field_map.put("review_text", this.review_text);
  }

  public void setField(String __fieldName, Object __fieldVal) {
    if (!setters.containsKey(__fieldName)) {
      throw new RuntimeException("No such field:"+__fieldName);
    }
    setters.get(__fieldName).setField(__fieldVal);
  }

}
