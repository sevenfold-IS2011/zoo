<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:workers">
		<h3>Employees description:</h3>
		<xsl:for-each select="zoo:employee">
		<div class="employee">
			<p> - - Name: <xsl:value-of select="zoo:name"/></p>
			<p>Username: <xsl:value-of select="zoo:username"/></p>
			<p>Gender: <xsl:value-of select="zoo:gender"/></p>
			<p>Age: <xsl:value-of select="zoo:age"/></p>
		</div>
		</xsl:for-each>
		<h3>Managers description:</h3>
		<xsl:for-each select="zoo:manager">
		<div class="manager">
			<p> - - Name: <xsl:value-of select="zoo:name"/></p>
			<p>Username: <xsl:value-of select="zoo:username"/></p>
			<p>Gender: <xsl:value-of select="zoo:gender"/></p>
			<p>Age: <xsl:value-of select="zoo:age"/></p>
			<p style="color:red">Salary: <xsl:value-of select="zoo:salary"/></p>
		</div>
		</xsl:for-each>
	</xsl:template>
</xsl:stylesheet>

