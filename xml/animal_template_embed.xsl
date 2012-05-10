<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:zoo">
		<h3>DAnimals descriptions:</h3>
			<xsl:for-each select="zoo:animal">
				<div class="animal">
				<p> -- Name: <xsl:value-of select="zoo:name"/></p>
				<p>Gender: <xsl:value-of select="zoo:gender"/></p>
				<p>Age: <xsl:value-of select="zoo:age"/></p>
				<p>Place: <xsl:value-of select="zoo:area/zoo:zona"/></p>
				<p>Species: <xsl:value-of select="zoo:area/zoo:species"/></p>
				</div>
			</xsl:for-each>
	</xsl:template>
</xsl:stylesheet>
