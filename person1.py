<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>456</width>
    <height>262</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>0</y>
      <width>151</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>24</pointsize>
      <weight>75</weight>
      <italic>false</italic>
      <bold>true</bold>
      <underline>true</underline>
      <strikeout>false</strikeout>
     </font>
    </property>
    <property name="text">
     <string>Log in</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>80</y>
      <width>51</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>username:</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>80</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>110</y>
      <width>51</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>password:</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_2">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>110</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>150</y>
      <width>56</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>next</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>456</width>
     <height>18</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections>
  <connection>
   <sender>pushButton</sender>
   <signal>clicked()</signal>
   <receiver>lineEdit_2</receiver>
   <slot>clear()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>172</x>
     <y>179</y>
    </hint>
    <hint type="destinationlabel">
     <x>189</x>
     <y>146</y>
    </hint>
   </hints>
  </connection>
  <connection>
   <sender>pushButton</sender>
   <signal>clicked()</signal>
   <receiver>lineEdit</receiver>
   <slot>clear()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>126</x>
     <y>178</y>
    </hint>
    <hint type="destinationlabel">
     <x>148</x>
     <y>102</y>
    </hint>
   </hints>
  </connection>
  <connection>
   <sender>pushButton</sender>
   <signal>clicked()</signal>
   <receiver>MainWindow</receiver>
   <slot>close()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>147</x>
     <y>176</y>
    </hint>
    <hint type="destinationlabel">
     <x>399</x>
     <y>299</y>
    </hint>
   </hints>
  </connection>
 </connections>
</ui>
